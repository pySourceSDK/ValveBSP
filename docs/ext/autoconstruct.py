
import os
from docutils import nodes
import sphinx
import construct
from sphinx.ext.autodoc import Documenter,  ModuleDocumenter, ModuleLevelDocumenter, ClassLevelDocumenter

from typing import cast

from sphinx import addnodes
from sphinx.locale import _, __
from sphinx.util.inspect import safe_getattr
from sphinx.util.docstrings import prepare_docstring
from sphinx.util.docfields import DocFieldTransformer
from sphinx.util.nodes import make_id
from sphinx.pycode import ModuleAnalyzer, PycodeError
from sphinx.domains import ObjType
from sphinx.domains.cpp import CPPDomain
from sphinx.domains.python import PythonDomain, PyXrefMixin, PyXRefRole, PyObject, PyVariable, PyAttribute, PyClasslike, PyField, PyTypedField
from sphinx.writers.html5 import HTML5Translator
from sphinx.builders.html import StandaloneHTMLBuilder
from sphinx.directives import ObjectDescription
from sphinx.util.fileutil import copy_asset
from docutils.parsers import rst

import mock

import ast
import sys
import executing

DOMAIN = 'con'
ALL = object()

VERBOSE = False


def Struct_mock__init__(self, *subcons, **subconskw):
    """
    This here is some introspection black magic. This init function is meant to
    replace Struct's __init__, only during documentation building.
    It will allow a struct to remember it's variable name.
    The Struct will take on the name of the variable it's defined as.
    """

    # Regular Init
    construct.core.Construct.__init__(self)
    self.subcons = list(subcons) + list(k/v for k, v in subconskw.items())
    self._subcons = construct.lib.Container((sc.name, sc)
                                            for sc in self.subcons if sc.name)
    self.flagbuildnone = all(sc.flagbuildnone for sc in self.subcons)

    # Additional init
    try:
        node = executing.Source.executing(sys._getframe(1)).node
        while hasattr(node, 'parent') and not isinstance(node, ast.Assign):
            node = node.parent
            assert not isinstance(node, ast.Module)
        if isinstance(node.targets[0], ast.Name):
            self.name = node.targets[0].id
        elif isinstance(node.targets[0], ast.Attribute):
            self.name = node.targets[0].attr
    except Exception as e:
        node = None


def getdoc(obj, attrgetter=safe_getattr, allow_inherited=False):
    """method to extract a Struct's doc, replacing it's docstring."""
    return obj.docs


def deconstruct(s, name=None, docs=None):
    """
    Can get through a chain of Construct.core.Renamed and
    will determine what the original struct was, and what to use
    as a name, struct name and docstring
    """
    if isinstance(s, construct.core.Renamed):
        name = name or safe_getattr(s, 'name')
        docs = docs or safe_getattr(s, 'docs')
        return deconstruct(s.subcon, name, docs)
    elif isinstance(s, construct.core.Struct):
        varname = safe_getattr(s, 'name', name)
        return s, name, varname, docs
    else:
        return s, name, None, docs


class ConstructDocumenter(Documenter):
    domain = DOMAIN
    member_order = 20

    def get_doc(self, encoding=None, ignore=1):
        # get the doctring
        docstring = getdoc(self.object, self.get_attr,
                           self.env.config.autodoc_inherit_docstrings)
        if docstring:
            tab_width = self.directive.state.document.settings.tab_width
            return [prepare_docstring(docstring, ignore, tab_width)]
        return []

    def import_object(self):
        # inject the new constructor into Struct
        with mock.patch.object(
                construct.core.Struct, '__init__', Struct_mock__init__):
            return super().import_object()


class SubconDocumenter(ConstructDocumenter, ClassLevelDocumenter):
    objtype = 'subcon'
    priority = 11

    @classmethod
    def can_document_member(cls, member, membername, isattr, parent):
        # determine if member can be documented
        return isinstance(member, construct.core.Construct) and \
            isinstance(parent, StructDocumenter) and isattr

    def add_directive_header(self, sig):
        # add construct specific headers
        Documenter.add_directive_header(self, sig)

        sourcename = self.get_sourcename()
        s, sname, srefname, sdoc = deconstruct(self.object)

        if isinstance(s, construct.core.FormatField):
            self.add_line('   :fieldtype: ' + s.fmtstr, sourcename)
        elif isinstance(s, construct.core.Struct) and srefname:
            self.add_line('   :structtype: ' + srefname, sourcename)
            link = ":con:struct:`" + srefname + '<' + srefname + '>`'

    def generate(self, *args, **kwargs):
        # generate makes rest formated output
        super().generate(*args, **kwargs)
        if VERBOSE:
            print('-----result------')
            for l in self.directive.result:
                print(l)


class StructDocumenter(ConstructDocumenter, ModuleLevelDocumenter):
    objtype = 'struct'
    priority = 1

    @classmethod
    def can_document_member(cls, member, membername, isattr, parent):
        # determine if member can be documented
        return isinstance(member, construct.core.Construct) and \
            isinstance(parent, ModuleDocumenter) and isattr

    def filter_members(self, members, want_all):
        # filter out members fields not to be documented
        return [(membername, member, True) for membername, member in members
                if not member == construct.core.Pass and
                not isinstance(member, construct.core.Padded)]

    def get_object_members(self, want_all):
        # create a list of members out of self.object
        s, name, refname, doc = deconstruct(self.object)
        return (False, [(sname, ssc) for ssc, sname, refname, sdoc in
                        [deconstruct(sc) for sc in s.subcons]])

    def document_members(self, all_members=False):
        # ModuleLevelDocumenter.document_members(self)

        # set current namespace for finding members
        self.env.temp_data['autodoc:module'] = self.modname
        if self.objpath:
            self.env.temp_data['autodoc:class'] = self.objpath[0]

        want_all = all_members or self.options.inherited_members or \
            self.options.members is ALL

        # find out which members are documentable
        members_check_module, members = self.get_object_members(want_all)

        # document non-skipped members
        memberdocumenters = []  # type: List[Tuple[Documenter, bool]]
        for (mname, member, isattr) in self.filter_members(members, want_all):
            classes = [cls for cls in self.documenters.values()
                       if cls.can_document_member(member, mname, isattr, self)]
            if not classes:
                # don't know how to document this member
                continue
            # prefer the documenter with the highest priority
            classes.sort(key=lambda cls: cls.priority)
            # give explicitly separated module name, so that members
            # of inner classes can be documented
            full_mname = self.modname + '::' + \
                '.'.join(self.objpath + [mname])
            documenter = classes[-1](self.directive, full_mname, self.indent)
            memberdocumenters.append((documenter, isattr))

        for documenter, isattr in memberdocumenters:
            documenter.generate(
                all_members=True, real_modname=self.real_modname,
                check_module=members_check_module and not isattr)

        # reset current objects
        self.env.temp_data['autodoc:module'] = None
        self.env.temp_data['autodoc:class'] = None


class desc_structref(nodes.Part, nodes.Inline, nodes.FixedTextElement):
    pass


class desc_pytype(nodes.Part, nodes.Inline, nodes.FixedTextElement):
    pass


class desc_ctype(nodes.Part, nodes.Inline, nodes.FixedTextElement):
    pass


class StructHTML5Translator(HTML5Translator):
    def visit_type(self, node):
        self.body.append(self.starttag(node, 'code', '',
                                       CLASS='sig-prename descclassname'))
        self.body.append('<span class="sig-paren">(</span>')

    def depart_type(self, node):
        self.body.append('<span class="sig-paren">)</span>')
        self.body.append('</code>')

    visit_desc_structref = visit_type
    depart_desc_structref = depart_type
    visit_desc_pytype = visit_type
    depart_desc_pytype = depart_type

    def visit_desc_ctype(self, node):
        self.body.append(self.starttag(node, 'code', '',
                                       CLASS='sig-prename descclassname',
                                       STYLE='color: gray'))
        self.body.append('<span>&ltparsed from ')

    def depart_desc_ctype(self, node):
        self.body.append('&gt</span>')
        self.body.append('</code>')


class StructStandaloneHTMLbuilder(StandaloneHTMLBuilder):
    @property
    def default_translator_class(self):
        return StructHTML5Translator


FF_TYPES = {
    # FormatField : (pytype, ctype)
    'e': ('float', '754 float'),
    'f': ('float', 'float'),
    'd': ('float', 'double'),
    'b': ('int', 'signed char'),
    'B': ('int', 'unsigned char'),
    'h': ('int', 'short'),
    'H': ('int', 'unsigned short'),
    'L': ('int', 'unsigned long'),
    'Q': ('int', 'integer'),
    'l': ('int', 'long'),
    'q': ('int', 'unsigned long long'),
}


def unformat(formatfieldstr):
    return FF_TYPES[formatfieldstr[1]]


class ConstructObjectDesc():
    domain = DOMAIN

    def add_target_and_index(self, name_cls, sig, signode):
        modname = self.options.get(
            'module', self.env.ref_context.get('py:module'))
        fullname = name_cls[0]
        node_id = make_id(self.env, self.state.document, '', fullname)

        # note target
        if fullname not in self.state.document.ids:
            signode['names'].append(fullname)
            signode['ids'].append(fullname)
            signode['first'] = (not self.names)
            self.state.document.note_explicit_target(signode)

            domain = cast(PythonDomain, self.env.get_domain(DOMAIN))
            domain.note_object(fullname, self.objtype, node_id)

        indextext = self.get_index_text(modname, name_cls)
        if indextext:
            self.indexnode['entries'].append(('single', indextext,
                                              fullname, '', None))


# PyObject > ObjectDescription > SphinxDirective > Directive > object
class Struct(ConstructObjectDesc, PyClasslike):
    option_spec = PyClasslike.option_spec.copy()


# PyObject > ObjectDescription > SphinxDirective > Directive > object
class Subcon(ConstructObjectDesc, PyAttribute):
    option_spec = PyAttribute.option_spec.copy()
    option_spec.update({
        'structtype': rst.directives.unchanged,
        'fieldtype': rst.directives.unchanged,
        'default_value': rst.directives.unchanged
    })

    def handle_signature(self, sig, signode):
        """ Almost there, this is for sure where the money happens.
         create new nodes and you'll get there for sure
        """
        fullname, prefix = super().handle_signature(sig, signode)
        structtype = self.options.get('structtype')
        if structtype:
            refnode = addnodes.pending_xref('', refdomain=DOMAIN, refexplicit=False,
                                            reftype='struct', reftarget=structtype)
            refnode += desc_structref(structtype, structtype)
            signode += refnode
        fieldtype = self.options.get('fieldtype')
        if fieldtype:
            pytype, ctype = unformat(fieldtype)

            pyref = addnodes.pending_xref('', refdomain='py', refexplicit=False,
                                          reftype='class', reftarget=pytype)
            pyref += desc_pytype(pytype, pytype)
            signode += pyref
            signode += desc_ctype(ctype, ctype)

        return fullname, prefix


class ConstructPythonDomain(PythonDomain):
    name = DOMAIN
    label = 'Construct'

    object_types = {'struct': ObjType(_('data'), 'data', 'obj'),
                    'subcon': ObjType(_('data'), 'data', 'obj')}
    directives = {'struct': Struct,
                  'subcon': Subcon}
    roles = {'struct': PyXRefRole(),
             'subcon': PyXRefRole()}


asset_files = ['autoconstruct.css']


def copy_asset_files(app, exc):
    ext_dir = os.path.abspath(os.path.dirname(__file__))
    if exc is None:  # build succeeded
        for asset in asset_files:
            asset_path = os.path.join(ext_dir, asset)
            copy_asset(asset_path, os.path.join(app.outdir, '_static'))
            app.add_css_file(asset)


def setup(app):
    app.add_builder(StructStandaloneHTMLbuilder, override=True)
    app.add_domain(ConstructPythonDomain)
    app.add_node(desc_structref)
    app.add_node(desc_pytype)
    app.add_node(desc_ctype)
    app.add_autodocumenter(StructDocumenter)
    app.add_autodocumenter(SubconDocumenter)

    for asset in asset_files:
        app.add_css_file(asset)
    app.connect('build-finished', copy_asset_files)

    return {'version': sphinx.__display_version__, 'parallel_read_safe': True}

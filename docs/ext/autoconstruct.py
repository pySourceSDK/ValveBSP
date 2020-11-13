
import os
from contextlib import contextmanager, ExitStack
from docutils import nodes
import sphinx
import construct
from sphinx.ext.autodoc import Documenter, ModuleDocumenter, ModuleLevelDocumenter, ClassLevelDocumenter

from typing import cast

from sphinx import addnodes
from sphinx.locale import _, __
from sphinx.util.inspect import safe_getattr, safe_getmembers
from sphinx.util.docstrings import prepare_docstring
from sphinx.util.docfields import DocFieldTransformer
from sphinx.util.nodes import make_id
from sphinx.pycode import ModuleAnalyzer, PycodeError
from sphinx.domains import ObjType
from sphinx.domains.cpp import CPPDomain
from sphinx.domains.python import PythonDomain, PyXrefMixin, PyXRefRole, PyObject, PyModule, PyVariable, PyAttribute, PyClasslike, PyField, PyTypedField
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

construct_overrides = [
    construct.core.Struct,
    construct.core.Renamed,
    construct.core.Aligned,
    construct.core.Array]

construct_inits = {}
for c in construct_overrides:
    construct_inits[c.__name__] = c.__init__


def Construct_mock__init__(self, *args, **kwargs):
    """
    This here is some introspection black magic to be injected in construct's
    init functions, only during documentation building.
    It allows construct class instances to remember a few things:
    1. The variable name they were instantiated as.
    2. The module they were defined as.
    """
    # Regular Init
    construct_inits[type(self).__name__](self, *args, **kwargs)

    # Additional init
    try:
        # Remember module is was declared in
        frame = sys._getframe(1)
        self.__module__ = frame.f_globals['__name__']
        # Remember name it was declared as
        node = executing.Source.executing(frame).node
        while hasattr(node, 'parent') and not isinstance(node, ast.Assign):
            node = node.parent
            assert not isinstance(node, ast.Module)
        if isinstance(node.targets[0], ast.Name):
            self.name = node.targets[0].id
        elif isinstance(node.targets[0], ast.Attribute):
            self.name = node.targets[0].attr
    except Exception as e:
        node = None


def Subconstruct_mock__getattr__(self, name):
    """
    makes sure Subconstruct has __getattr__,
    otherwise introspection is impossible"""
    return getattr(self.subcon, name)


@contextmanager
def mocked_constructs():
    """A context to apply all the Construct mocks"""
    with ExitStack() as es:
        for x in construct_overrides:
            minit = mock.patch.object(x,
                                      '__init__', Construct_mock__init__)
            es.enter_context(minit)
        mgetattr = mock.patch.object(construct.core.Subconstruct,
                                     '__getattr__', Subconstruct_mock__getattr__,
                                     create=True)
        es.enter_context(mgetattr)
        yield


def getdoc(obj, attrgetter=safe_getattr, allow_inherited=False):
    """method to extract a Struct's doc, replacing it's docstring."""
    return obj.docs


def deconstruct(s, name=None, docs=None, count=None):
    """
    Can get through a chain of Construct.core.Subcontruct and
    will determine what the original struct was, and what to use
    as a name, struct name, docstring and possibly count
    """
    if isinstance(s, construct.core.Array):
        count = count or []
        if isinstance(s.count, int):
            count = [s.count] + count
        else:
            count = [''] + count
    if isinstance(s, construct.core.Subconstruct):
        name = name or safe_getattr(s, 'name')
        docs = docs or safe_getattr(s, 'docs')
        return deconstruct(s.subcon, name, docs, count)
    elif isinstance(s, construct.core.Struct):
        varname = safe_getattr(s, 'name', name)
        return s, name, varname, docs, count
    else:
        return s, name, None, docs, count


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
        with mocked_constructs():
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
        s, sname, srefname, sdoc, count = deconstruct(self.object)

        suffix = ''
        if count:
            suffix = ', [' + ']['.join([str(c) for c in count]) + ']'
        if isinstance(s, construct.core.FormatField):
            self.add_line('   :fieldtype: ' + s.fmtstr + suffix, sourcename)
        elif isinstance(s, construct.core.Struct) and srefname:
            self.add_line('   :structtype: ' + srefname + suffix, sourcename)

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
        s, name, refname, doc, count = deconstruct(self.object)
        return (False, [(sname, ssc) for ssc, sname, refname, sdoc in
                        [deconstruct(sc)[:4] for sc in s.subcons]])

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


class ModconDocumenter(ModuleDocumenter):
    objtype = 'modcon'

    def add_directive_header(self, sig):
        return

    def import_object(self):
        with mocked_constructs():
            return super().import_object()

    def filter_members(self, members, want_all):
        ret = []
        for mname, member in members:
            if self.object.__name__ == member.__module__:
                ret.append((mname, member, True))
        return ret

    def get_object_members(self, want_all):
        ret = []

        def isStruct(i):
            isS = isinstance(i, construct.core.Struct)
            isS = isS or isinstance(i, construct.core.Aligned)
            isS = isS or isinstance(i, construct.core.Renamed)
            return isS

        for mname, member in safe_getmembers(self.object, isStruct):
            ret.append((mname, safe_getattr(self.object, mname)))

        return False, ret


class desc_subcon(nodes.Part, nodes.Inline, nodes.FixedTextElement):
    pass


class desc_stype(nodes.Part, nodes.Inline, nodes.FixedTextElement):
    def astext(self):
        return '({})'.format(super().astext())


class desc_structref(desc_stype):
    pass


class desc_pytype(desc_stype):
    pass


class desc_count(nodes.Part, nodes.Inline, nodes.FixedTextElement):
    def astext(self):
        return '[{}]'.format(super().astext())


class desc_ctype(nodes.Part, nodes.Inline, nodes.FixedTextElement):
    def astext(self):
        return '<parsed from {}>'.format(super().astext())


class StructHTML5Translator(HTML5Translator):

    def visit_desc_subcon(self, node):
        self.body.append(self.starttag(node, 'code', '',
                                       CLASS='sig-prename descclassname'))
        self.body.append('<span class="sig-paren">(</span>')

    def depart_desc_subcon(self, node):
        self.body.append('<span class="sig-paren">)</span></code>')

    def visit_type(self, node):
        self.body.append(self.starttag(node, 'code', '',
                                       CLASS='sig-prename descclassname'))

    def depart_type(self, node):
        self.body.append('</code>')

    visit_desc_structref = visit_type
    depart_desc_structref = depart_type
    visit_desc_pytype = visit_type
    depart_desc_pytype = depart_type

    def visit_desc_ctype(self, node):
        self.body.append(self.starttag(node, 'span', '',
                                       STYLE='color: gray'))
        self.body.append('&ltparsed from ')

    def depart_desc_ctype(self, node):
        self.body.append('&gt</span>')

    def visit_desc_count(self, node):
        pass

    def depart_desc_count(self, node):
        pass


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


def unformatCount(formatfieldstr):
    unformated = tuple(formatfieldstr.rsplit(', ', 1))
    if len(unformated) == 1:
        unformated += (None,)
    return unformated


def unformatFieldType(formatfieldstr):
    unformated = unformatCount(formatfieldstr)
    return FF_TYPES[unformated[0][1]] + (unformated[-1],)


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


class Struct(ConstructObjectDesc, PyClasslike):
    option_spec = PyClasslike.option_spec.copy()


class Subcon(ConstructObjectDesc, PyAttribute):
    option_spec = PyAttribute.option_spec.copy()
    option_spec.update({
        'structtype': rst.directives.unchanged,
        'fieldtype': rst.directives.unchanged,
        'default_value': rst.directives.unchanged
    })

    def handle_signature(self, sig, signode):
        fullname, prefix = super().handle_signature(sig, signode)
        structtype = self.options.get('structtype')
        if structtype:
            stype, count = unformatCount(structtype)
            subconnode = desc_subcon()
            refnode = addnodes.pending_xref('', refdomain=DOMAIN, refexplicit=False,
                                            reftype='struct', reftarget=stype)
            refnode += desc_structref(stype, stype)
            subconnode += refnode
            if count:
                subconnode += desc_count(count, count)
            signode += subconnode
        fieldtype = self.options.get('fieldtype')
        if fieldtype:
            pytype, ctype, count = unformatFieldType(fieldtype)

            subconnode = desc_subcon()
            refnode = addnodes.pending_xref('', refdomain='py', refexplicit=False,
                                            reftype='class', reftarget=pytype)
            refnode += desc_pytype(pytype, pytype)
            subconnode += refnode
            if count:
                subconnode += desc_count(count, count)
            signode += subconnode
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
    app.add_node(desc_count)
    app.add_node(desc_subcon)
    app.add_autodocumenter(ModconDocumenter)
    app.add_autodocumenter(StructDocumenter)
    app.add_autodocumenter(SubconDocumenter)

    for asset in asset_files:
        app.add_css_file(asset)
    app.connect('build-finished', copy_asset_files)

    return {'version': sphinx.__display_version__, 'parallel_read_safe': True}

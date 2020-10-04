
import sphinx
import construct
from sphinx.ext.autodoc import Documenter,  ModuleDocumenter, ModuleLevelDocumenter, ClassLevelDocumenter

from sphinx.locale import _, __
from sphinx.util.inspect import safe_getattr
from sphinx.util.docstrings import prepare_docstring
from sphinx.domains import ObjType
from sphinx.domains.python import PythonDomain, PyVariable, PyXRefRole
from docutils.parsers import rst

import mock
import ast
import sys
import executing

DOMAIN = 'con'


def Struct_mock__init__(self, *subcons, **subconskw):
    """
    This here is some black magic. This is init function is meant to
    replace Struct's __init__, only during documentation building.
    It will allow a struct to remember it's name.
    The Struct will take on the name of the variable it's defined in.
    """
    # Regular things
    construct.core.Construct.__init__(self)
    self.subcons = list(subcons) + list(k/v for k, v in subconskw.items())
    self._subcons = construct.lib.Container((sc.name, sc)
                                            for sc in self.subcons if sc.name)
    self.flagbuildnone = all(sc.flagbuildnone for sc in self.subcons)

    # Added things
    try:
        node = executing.Source.executing(sys._getframe(2)).node
        while hasattr(node, 'parent') and not isinstance(node, ast.Assign):
            node = node.parent
        if isinstance(node.targets[0], ast.Name):
            self.name = node.targets[0].id
        elif isinstance(node.targets[0], ast.Attribute):
            self.name = node.targets[0].attr
    except:
        node = None


def getdoc(obj, attrgetter=safe_getattr, allow_inherited=False):
    """ method to extract a Struct's doc, replacing it's docstring."""
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
            self.add_line('   :ctype: ' + s.fmtstr, sourcename)
        elif isinstance(s, construct.core.Struct) and srefname:
            self.add_line('   :reftype: ' + srefname, sourcename)


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


class PyConstruct(PyVariable):
    option_spec = PyVariable.option_spec.copy()
    option_spec.update({
        'ctype': rst.directives.unchanged,
        'reftype': rst.directives.unchanged,
        'default_value': rst.directives.unchanged
    })


class ConstructPythonDomain(PythonDomain):
    name = DOMAIN
    label = 'Construct'

    object_types = {'struct': ObjType(_('data'), 'data', 'obj'),
                    'subcon': ObjType(_('data'), 'data', 'obj')}
    directives = {'struct': PyConstruct,
                  'subcon': PyConstruct}
    roles = {'struct': PyXRefRole(),
             'subcon': PyXRefRole()}

    def __init__(self, env):
        super().__init__(env)


def setup(app):
    app.add_domain(ConstructPythonDomain)
    app.add_autodocumenter(StructDocumenter)
    app.add_autodocumenter(SubconDocumenter)

    return {'version': sphinx.__display_version__, 'parallel_read_safe': True}

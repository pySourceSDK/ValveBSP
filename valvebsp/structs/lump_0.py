"""
Lump 0 - Entities
=================

This lump is simply one long string containing all entities in a format similar to vmf.

ValveBsp will parse this string into a list of entities, represented as lists of properties.
"""
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals
from future import standard_library
standard_library.install_aliases()

from construct import *  # NOQA: #402
import pyparsing as pp   # NOQA: E402
from valvebsp.structs.common import *  # NOQA: #402


entity_property_encoding = pp.Group(pp.QuotedString('"') * 2)
entity_encoding = pp.nestedExpr('{', '}', entity_property_encoding, None)
lump_0_encoding = pp.ZeroOrMore(entity_encoding)


class EntityEncoder(Adapter):

    def _decode(self, obj, context, path):
        return lump_0_encoding.parseString(obj).asList()

    def _encode(self, obj, context, path):
        estr = ''
        for ent in obj:
            estr += '{\n'
            for entp in ent:
                estr += '"' + entp[0] + '" "' + entp[1] + '"\n'
            estr += '}\n'
        estr += '\0'
        return estr


@lump_version(0)
def lump_0(header, profile=None):
    return EntityEncoder(GreedyString("ascii"))

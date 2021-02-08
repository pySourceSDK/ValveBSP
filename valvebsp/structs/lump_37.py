"""
Lump 37 - Primitives
====================

This lump contains an array of :any:`dprimitive_t`.
"""

from __future__ import division
from __future__ import absolute_import
from __future__ import print_function
from __future__ import unicode_literals
from future import standard_library
standard_library.install_aliases()

from construct import *  # NOQA: #402
from valvebsp.constants import *  # NOQA: #402
from valvebsp.exceptions import *  # NOQA: #402
from valvebsp.structs.common import *  # NOQA #402

dprimitive_type = Enum(
    Int8ul,
    PRIM_TRILIST=0,
    PRIM_TRISTRIP=1,
)

dprimitive_t = Aligned(2, Struct(
    'type' / dprimitive_type,
    'firstIndex' / Int16ul * 'refers to lump_39',
    'indexCount' / Int16ul,
    'firstVert' / Int16ul * 'refers to lump_38',
    'vertCount' / Int16ul,
))


def lump_37(header, profile=None):
    if header.version != 0:
        raise LumpVersionUnsupportedError(header.version)
    return lump_array(LUMP_PRIMITIVES, dprimitive_t, header)

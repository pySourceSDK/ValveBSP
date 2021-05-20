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
from valvebsp.structs.common import *  # NOQA #402

dprimitive_type = Enum(
    Int8ul,
    PRIM_TRILIST=0,
    PRIM_TRISTRIP=1,
)

dprimitive_t = Aligned(2, Struct(
    'type' / dprimitive_type,
    'firstIndex' / Int16ul * "index into :ref:`lump 39<lump_39>`",
    'indexCount' / Int16ul,
    'firstVert' / Int16ul * "index into :ref:`lump 38<lump_38>`",
    'vertCount' / Int16ul,
))


@lump_array
@lump_version(0)
def lump_37(header, profile=None):
    return dprimitive_t

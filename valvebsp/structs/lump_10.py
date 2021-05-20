"""
Lump 10 - Leafs
===============

This lump contains an array of :any:`dleaf_tV1` or :any:`dleaf_tV1` (Version detection is automatic).
"""

from __future__ import division
from __future__ import absolute_import
from __future__ import print_function
from __future__ import unicode_literals
from future import standard_library
standard_library.install_aliases()

from construct import *  # NOQA: #402
from valvebsp.structs.common import *  # NOQA: #402

dleaf_flags9 = FlagsEnum(BitsInteger(9),
                         LEAF_FLAGS_SKY=1,
                         LEAF_FLAGS_RADIAL=2,
                         LEAF_FLAGS_SKY2D=4,
                         LEAF_FLAGS_CONTAINS_DETAILOBJECTS=8)

dleaf_tV0 = Aligned(4, Bitwise(Struct(
    'contents' / Bytewise(Int32sl),
    'cluster' / Bytewise(Int16sl),

    'area' / BitsInteger(7),
    'flags' / dleaf_flags9,

    'mins' / Bytewise(Int16sl[3]),
    'maxs' / Bytewise(Int16sl[3]),

    'firstLeafFace' / Bytewise(Int16ul) * "index into :ref:`lump 16<lump_16>`",
    'numLeafFaces' / Bytewise(Int16ul),

    'firstLeafBrush' / Bytewise(Int16ul) * "index into :ref:`lump 17<lump_17>`",
    'numLeafBrushes' / Bytewise(Int16ul),
    'leafWaterDataID' / Bytewise(Int16sl) *
    "index into :ref:`lump 36<lump_36>`",

    'ambientLighting' / Bytewise(CompressedLightCube)
)))

dleaf_tV1 = Aligned(4, Bitwise(Struct(
    'contents' / Bytewise(Int32sl),
    'cluster' / Bytewise(Int16sl),

    'area' / BitsInteger(7),
    'flags' / dleaf_flags9,

    'mins' / Bytewise(Int16sl[3]),
    'maxs' / Bytewise(Int16sl[3]),


    'firstLeafFace' / Bytewise(Int16ul) * "index into :ref:`lump 16<lump_16>`",
    'numLeafFaces' / Bytewise(Int16ul),

    'firstLeafBrush' / Bytewise(Int16ul) * "index into :ref:`lump 17<lump_17>`",
    'numLeafBrushes' / Bytewise(Int16ul),
    'leafWaterDataID' / Bytewise(Int16sl) * "index into :ref:`lump 36<lump_36>`"
)))


@lump_array
@lump_version([0, 1])
def lump_10(header, profile=None):
    if header.version == 0:
        return dleaf_tV0
    elif header.version == 1:
        return dleaf_tV1

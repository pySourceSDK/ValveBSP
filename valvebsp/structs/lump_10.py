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
from valvebsp.constants import *  # NOQA: #402
from valvebsp.exceptions import *  # NOQA: #402
from valvebsp.structs.common import *  # NOQA: #402


dleaf_tV0 = Bitwise(Struct(
    'contents' / Bytewise(Int32sl),
    'cluster' / Bytewise(Int16sl),

    'area' / BitsInteger(7),
    'flags' / BitsInteger(9),

    'unknown' / Bytewise(Int16sl),

    'mins' / Bytewise(Int16sl[3]),
    'maxs' / Bytewise(Int16sl[3]),

    'firstLeafFace' / Bytewise(Int16ul),
    'numLeafFaces' / Bytewise(Int16ul),

    'firstLeafBrush' / Bytewise(Int16ul),
    'numLeafBrushes' / Bytewise(Int16ul),
    'leafWaterDataID' / Bytewise(Int16sl),

    'ambientLighting' / Bytewise(CompressedLightCube)
))

dleaf_tV1 = Bitwise(Struct(
    'contents' / Bytewise(Int32sl),
    'cluster' / Bytewise(Int16sl),

    'area' / BitsInteger(7),
    'flags' / BitsInteger(9),

    'unknown' / Bytewise(Int16sl),

    'mins' / Bytewise(Int16sl[3]),
    'maxs' / Bytewise(Int16sl[3]),

    'firstLeafFace' / Bytewise(Int16ul),
    'numLeafFaces' / Bytewise(Int16ul),

    'firstLeafBrush' / Bytewise(Int16ul),
    'numLeafBrushes' / Bytewise(Int16ul),
    'leafWaterDataID' / Bytewise(Int16sl)
))


def lump_10(header, profile=None):
    if header.version == 0:
        return lump_array(LUMP_LEAFS, dleaf_tV0, header)
    elif header.version == 1:
        return lump_array(LUMP_LEAFS, dleaf_tV1, header)
    else:
        raise LumpVersionUnsupportedError(header.version)

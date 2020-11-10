"""
Lump 10 - Leafs
===============
"""

from __future__ import division
from __future__ import absolute_import
from __future__ import print_function
from __future__ import unicode_literals
from future import standard_library
standard_library.install_aliases()

from construct import *  # NOQA: #402
from bsptools.constants import *  # NOQA: #402
from bsptools.exceptions import *  # NOQA: #402
from bsptools.structs.common_struct import *  # NOQA: #402


dleaf_tV0 = Struct(
    'contents' / Int32sl,
    'cluster' / Int16sl,


    'areaflag' / BitStruct(
        'area' / BitsInteger(7),
        'flags' / BitsInteger(9)),
    'unknown' / Int16sl,

    'mins' / Int16sl[3],
    'maxs' / Int16sl[3],

    'firstLeafFace' / Int16ul,
    'numLeafFaces' / Int16ul,

    'firstLeafBrush' / Int16ul,
    'numLeafBrushes' / Int16ul,
    'leafWaterDataID' / Int16sl,

    'ambientLighting' / CompressedLightCube
)

dleaf_tV1 = Struct(
    'contents' / Int32sl,
    'cluster' / Int16sl,


    'areaflag' / BitStruct(
        'area' / BitsInteger(7),
        'flags' / BitsInteger(9)),
    'unknown' / Int16sl,

    'mins' / Int16sl[3],
    'maxs' / Int16sl[3],

    'firstLeafFace' / Int16ul,
    'numLeafFaces' / Int16ul,

    'firstLeafBrush' / Int16ul,
    'numLeafBrushes' / Int16ul,
    'leafWaterDataID' / Int16sl
)


def lump_10(header, profile=None):
    if header.version == 0:
        return lump_array(LUMP_LEAFS, dleaf_tV0, header)
    elif header.version == 1:
        return lump_array(LUMP_LEAFS, dleaf_tV1, header)
    else:
        raise LumpVersionUnsupportedError(header.version)

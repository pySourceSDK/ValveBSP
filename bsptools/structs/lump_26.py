from __future__ import division
from __future__ import absolute_import
from __future__ import print_function
from __future__ import unicode_literals
from future import standard_library
standard_library.install_aliases()

from construct import *  # NOQA: #402
from bsptools.constants import *  # NOQA: #402
from bsptools.exceptions import *  # NOQA: #402
from bsptools.structs.common_struct import *  # NOQA #402

NeighborSpan = Enum(
    Int8sl,
    CORNER_TO_CORNER=0,
    CORNER_TO_MIDPOINT=1,
    MIDPOINT_TO_CORNER=2
)

NeighborOrientation = Enum(
    Int8sl,
    ORIENTATION_CCW_0=0,
    ORIENTATION_CCW_90=1,
    ORIENTATION_CCW_180=2,
    ORIENTATION_CCW_270=3
)

CDispSubNeighbor = Struct(
    # 'm_iNeighbor' / Int16ul,
    # 'm_NeighborOrientation' / NeighborOrientation,
    # 'm_Span' / NeighborSpan,
    # 'm_NeighborSpan' / NeighborSpan
    # The fields seem to be misordered, this is my best guess
    'm_Span' / NeighborSpan,
    'm_NeighborSpan' / NeighborSpan,
    'm_iNeighbor' / Int16ul,
    'unknown' / Byte,

    'm_NeighborOrientation' / NeighborOrientation,
)

CDispNeighbor = Struct(
    'm_SubNeighbors' / CDispSubNeighbor[2],
)

CDispCornerNeighbors = Struct(
    'm_Neighbors' / Int16ul[MAX_DISP_CORNER_NEIGHBORS],
    'm_nNeighbors' / Int8ul
)

ddispinfo_t = Struct(
    'startPosition' / Vector,
    'm_iDispVertStart' / Int32sl,
    'm_iDispTriStart'/Int32sl,

    'power' / Int32sl,
    'minTess'/Int32sl,
    'smoothingAngle' / Float32l,
    'contents'/Int32sl,

    'm_iMapFace' / Int16ul,

    'm_iLightmapAlphaStart' / Int32sl,
    'm_iLightmapSamplePositionStart' / Int32sl,

    'm_EdgeNeighbors' / CDispNeighbor[4],
    'm_CornerNeighbors' / CDispCornerNeighbors[4],

    'unknown' / Bytes(6),


    'm_AllowedVerts' / Int32ul[ALLOWEDVERTS_SIZE],
)


def lump_26(version):
    if version != 0:
        raise LumpVersionUnsupportedError(version)
    return lump_array(LUMP_DISPINFO, ddispinfo_t)

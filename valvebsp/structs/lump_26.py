"""
Lump 26 - Disp Info
===================

This lump contains an array of :any:`ddispinfo_t`
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
    'span' / NeighborSpan,
    'neighborSpan' / NeighborSpan,
    'neighbor' / Int16ul,
    'unknown' / Byte,

    'neighborOrientation' / NeighborOrientation,
)

CDispNeighbor = Struct(
    'subNeighbors' / CDispSubNeighbor[2],
)

CDispCornerNeighbors = Struct(
    'neighbors' / Int16ul[MAX_DISP_CORNER_NEIGHBORS],
    'nNeighbors' / Int8ul
)

ddispinfo_t = Struct(
    'startPosition' / Vector,
    'dispVertStart' / Int32sl,
    'dispTriStart'/Int32sl,

    'power' / Int32sl,
    'minTess'/Int32sl,
    'smoothingAngle' / Float32l,
    'contents'/Int32sl,

    'mapFace' / Int16ul,

    'lightmapAlphaStart' / Int32sl,
    'lightmapSamplePositionStart' / Int32sl,

    'edgeNeighbors' / CDispNeighbor[4],
    'cornerNeighbors' / CDispCornerNeighbors[4],

    'unknown' / Bytes(6),

    'allowedVerts' / Int32ul[ALLOWEDVERTS_SIZE],
)


def lump_26(header, profile=None):
    if header.version != 0:
        raise LumpVersionUnsupportedError(header.version)
    return lump_array(LUMP_DISPINFO, ddispinfo_t, header)

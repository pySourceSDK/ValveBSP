"""
Lump 45 - Overlays
==================

This lump contains an array of :any:`doverlay_t`.
"""

from __future__ import division
from __future__ import absolute_import
from __future__ import print_function
from __future__ import unicode_literals
from future import standard_library
standard_library.install_aliases()

from construct import *  # NOQA: #402
from valvebsp.structs.common import *  # NOQA #402

doverlay_t = Struct(
    'id' / Int32sl,
    'texInfo' / Int16sl * "index into :ref:`lump 6<lump_6>`",
    'faceCountAndRenderOrder' / Int16ul,
    'faces' / Int32sl[OVERLAY_BSP_FACE_COUNT],
    'u' / Float32l[2],
    'v' / Float32l[2],
    'UVPoints' / Vector[4],
    'origin' / Vector,
    'basisNormal' / Vector
)


@lump_array
@lump_version(0)
def lump_45(header, profile=None):
    return doverlay_t

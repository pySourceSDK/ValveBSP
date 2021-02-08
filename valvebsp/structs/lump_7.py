"""
Lump 7 - Faces
==============

This lump contains an array of :any:`dface_t`.
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

dface_t = Struct(
    'planenum' / Int16ul,
    'side' / Byte,
    'onNode' / Byte,
    'firstedge' / Int32sl,
    'numedges' / Int16sl,
    'texinfo' / Int16sl,
    'dispinfo' / Int16sl,
    'surfaceFogVolumeID' / Int16sl,
    'styles' / Byte[4],
    'lightofs' / Int32sl,
    'area' / Float32l,
    'lightmapTextureMinsInLuxels' / Int32sl[2],
    'lightmapTextureSizeInLuxels' / Int32sl[2],
    'origFace' / Int32sl,
    'numPrims' / Int16ul,
    'firstPrimID' / Int16ul,
    'smoothingGroups' / Int32ul,
)


def lump_7(header, profile=None):
    if header.version in [0, 1]:
        return lump_array(LUMP_FACES, dface_t, header)
    else:
        raise LumpVersionUnsupportedError(header.version)

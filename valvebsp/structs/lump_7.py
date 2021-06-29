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
from valvebsp.structs.common import *  # NOQA: #402

dface_t = Struct(
    'planenum' / Int16ul,
    'side' / Byte,
    'onNode' / Byte,
    'firstedge' / Int32sl * "index into :ref:`lump 13<lump_13>`",
    'numedges' / Int16sl,
    'texinfo' / Int16sl * "index into :ref:`lump 6<lump_6>`",
    'dispinfo' / Int16sl * "index into :ref:`lump 26<lump_26>`",
    'surfaceFogVolumeID' / Int16sl,
    'styles' / Byte[4],
    'lightofs' / Int32sl * "index into :ref:`lump 8<lump_8>`",
    'area' / Float32l,
    'lightmapTextureMinsInLuxels' / Int32sl[2],
    'lightmapTextureSizeInLuxels' / Int32sl[2],
    'origFace' / Int32sl * "index into :ref:`lump 11<lump_11>`",
    'numPrims' / Int16ul,
    'firstPrimID' / Int16ul * "index into :ref:`lump 37<lump_37>`",
    'smoothingGroups' / Int32ul,
)


@lump_array
@lump_version([0, 1])
def lump_7(header, profile=None):
    return dface_t

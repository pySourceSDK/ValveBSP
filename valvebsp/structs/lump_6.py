"""
Lump 6 - Texture Info
=====================

This lump contains an array of :any:`texinfo_t`.
"""

from __future__ import division
from __future__ import absolute_import
from __future__ import print_function
from __future__ import unicode_literals
from future import standard_library
standard_library.install_aliases()

from construct import *  # NOQA: #402
from valvebsp.structs.common import *  # NOQA: #402

texinfo_flags8 = FlagsEnum(Int32ul,
                           SURF_LIGHT=1,
                           SURF_SKY2D=2,
                           SURF_SKY=4,
                           SURF_WARP=8,
                           SURF_TRANS=16,
                           SURF_NOPORTAL=32,
                           SURF_TRIGGER=64,
                           SURF_NODRAW=128,
                           SURF_HINT=256,
                           SURF_SKIP=512,
                           SURF_NOLIGHT=1024,
                           SURF_BUMPLIGHT=2048,
                           SURF_NOSHADOWS=4096,
                           SURF_NODECALS=8192,
                           SURF_NOCHOP=16384,
                           SURF_HITBOX=32768)
texinfo_t = Struct(
    'textureVecsTexelsPerWorldUnits' / Float32l[2][4],
    'lightmapVecsLuxelsPerWorldUnits' / Float32l[2][4],
    'flags' / texinfo_flags8,
    'texData' / Int32sl * 'index into :ref:`lump 2<lump_2>`',
)


@lump_array
@lump_version(0)
def lump_6(header, profile=None):
    return texinfo_t

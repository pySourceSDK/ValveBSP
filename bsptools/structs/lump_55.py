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

CompressedLightCube = Struct(
    'm_color' / ColorRGBExp32[6]
)

dleafambientlighting_t = Aligned(4, Struct(
    'cube' / CompressedLightCube,
    'x' / Byte,
    'y' / Byte,
    'z' / Byte
))


def lump_55(version):
    if version == 1:
        return lump_array(LUMP_LEAF_AMBIENT_LIGHTING_HDR,
                          dleafambientlighting_t)
    else:
        raise LumpVersionUnsupportedError(version)

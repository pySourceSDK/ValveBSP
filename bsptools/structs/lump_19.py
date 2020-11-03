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


dbrushside_t = Struct(
    'planeNum' / Int16ul,
    'texInfo' / Int16sl,
    'dispInfo' / Int16sl,
    'bevel' / Int16sl
)
dbrushside_t_P2 = Struct(
    'planeNum' / Int16ul,
    'texInfo' / Int16sl,
    'dispInfo' / Int16sl,
    'bevel' / Int8sl,
    'thin' / Int8sl
)


def lump_19(header, profile=None):
    if header.version == 0:
        if profile in [ALIENSWARM, PORTAL2]:
            return lump_array(LUMP_BRUSHSIDES, dbrushside_t_P2, header)
        else:
            return lump_array(LUMP_BRUSHSIDES, dbrushside_t, header)
    else:
        raise LumpVersionUnsupportedError(header.version)

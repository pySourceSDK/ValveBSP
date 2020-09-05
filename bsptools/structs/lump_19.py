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
    'planenum' / Int16ul,
    'texinfo' / Int16sl,
    'dispinfo' / Int16sl,
    'bevel' / Int16sl
)


def lump_19(header):
    if header.version != 0:
        raise LumpVersionUnsupportedError(header.version)
    return lump_array(LUMP_BRUSHSIDES, dbrushside_t, header)

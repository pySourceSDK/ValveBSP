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

dleaf_t = Struct(
    'contents' / Int32sl,
    'cluster' / Int16sl,


    'areaflag' / BitStruct(
        'area' / BitsInteger(7),
        'flags' / BitsInteger(9)),
    'unknown' / Int16sl,

    'mins' / Int16sl[3],
    'maxs' / Int16sl[3],

    'firstleafface' / Int16ul,
    'numleaffaces' / Int16ul,

    'firstleafbrush' / Int16ul,
    'numleafbrushes' / Int16ul,
    'leafWaterDataID' / Int16sl
)


def lump_10(version):
    if version == 1:
        return lump_array(LUMP_LEAFS, dleaf_t)
    else:
        raise LumpVersionUnsupportedError(version)

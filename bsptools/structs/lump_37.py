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

dprimitive_type = Enum(
    Int8ul,
    PRIM_TRILIST=0,
    PRIM_TRISTRIP=1,
)

dprimitive_t = Aligned(2, Struct(
    'type' / dprimitive_type,
    'firstIndex' / Int16ul,
    'indexCount' / Int16ul,
    'firstVert' / Int16ul,
    'vertCount' / Int16ul,
))


def lump_37(version):
    if version != 0:
        raise LumpVersionUnsupportedError(version)
    return lump_array(LUMP_PRIMITIVES, dprimitive_t)

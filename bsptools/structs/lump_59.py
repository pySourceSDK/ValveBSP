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

flags_t = Struct('levelFlags' / Int32ul)


def lump_59(header):
    if header.version != 0:
        raise LumpVersionUnsupportedError(header.version)
    return lump_struct(LUMP_MAP_FLAGS, flags_t, header)

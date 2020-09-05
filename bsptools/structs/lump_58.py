from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals
from future import standard_library
standard_library.install_aliases()

from construct import *  # NOQA: #402
from bsptools.constants import *  # NOQA: #402
from bsptools.exceptions import *  # NOQA: #402
from bsptools.structs.common_struct import *  # NOQA #402
from bsptools.structs.lump_7 import dface_t  # NOQA #402


def lump_58(header):
    if header.version in [0, 1]:
        return lump_array(LUMP_FACES_HDR, dface_t, header)
    else:
        raise LumpVersionUnsupportedError(header.version)

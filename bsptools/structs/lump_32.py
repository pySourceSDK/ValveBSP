from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals
from future import standard_library
standard_library.install_aliases()

from bsptools.constants import *  # NOQA: #402
from bsptools.exceptions import *  # NOQA: #402
from bsptools.structs.common_struct import *  # NOQA #402


def lump_32(header, profile=None):
    if header.version != 0:
        raise LumpVersionUnsupportedError(header.version)
    return lump_bytes(LUMP_DISP_LIGHTMAP_ALPHAS, header)
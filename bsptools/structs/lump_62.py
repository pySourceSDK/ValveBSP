from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals
from future import standard_library
standard_library.install_aliases()

from bsptools.constants import *  # NOQA: #402
from bsptools.exceptions import *  # NOQA: #402
from bsptools.structs.common_struct import *  # NOQA #402


def lump_62(header, profile=None):
    if header.filelen == 0:
        return lump_dud(LUMP_PHYSLEVEL, header)
    if header.version == 0:
        return lump_bytes(LUMP_PHYSLEVEL, header)
    else:
        raise LumpVersionUnsupportedError(header.version)

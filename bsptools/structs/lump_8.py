"""
Lump 8 - Lighting
=================
"""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals
from future import standard_library
standard_library.install_aliases()

from construct import *  # NOQA: #402
from bsptools.constants import *  # NOQA: #402
from bsptools.exceptions import *  # NOQA: #402
from bsptools.structs.common_struct import *  # NOQA: #402


def lump_8(header, profile=None):
    if header.version in [0, 1]:
        return lump_array(LUMP_LIGHTING, ColorRGBExp32, header)
    else:
        raise LumpVersionUnsupportedError(header.version)

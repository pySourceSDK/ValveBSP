"""
Lump 17 - Leaf Brushes
======================

This lump contains an array of :any:`Int<int>`. They are references to brush ids in :any:`lump_18<lump_18>`.
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
from bsptools.structs.common import *  # NOQA: #402


def lump_17(header, profile=None):
    if header.version != 0:
        raise LumpVersionUnsupportedError(header.version)
    return lump_array(LUMP_LEAFBRUSHES, Int16ul, header)

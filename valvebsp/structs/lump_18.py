"""
Lump 18 - Brushes
=================

This lump contains an array of :any:`dbrush_t`.
"""

from __future__ import division
from __future__ import absolute_import
from __future__ import print_function
from __future__ import unicode_literals
from future import standard_library
standard_library.install_aliases()

from construct import *  # NOQA: #402
from valvebsp.constants import *  # NOQA: #402
from valvebsp.exceptions import *  # NOQA: #402
from valvebsp.structs.common import *  # NOQA: #402

dbrush_t = Struct(
    'firstSide' / Int32sl,
    'numSides' / Int32sl,
    'contents' / Int32sl,
)


def lump_18(header, profile=None):
    if header.version != 0:
        raise LumpVersionUnsupportedError(header.version)
    return lump_array(LUMP_BRUSHES, dbrush_t, header)

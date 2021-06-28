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
from valvebsp.structs.common import *  # NOQA: #402
from valvebsp.structs.flags import contents_flags32  # NOQA: #402

dbrush_t = Struct(
    'firstSide' / Int32sl * "index into :ref:`lump 19<lump_19>`",
    'numSides' / Int32sl,
    'contents' / contents_flags32,
)


@lump_array
@lump_version(0)
def lump_18(header, profile=None):
    return dbrush_t

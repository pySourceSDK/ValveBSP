"""
Lump 12 - Edges
===============

This lump contains an array of :any:`dedge_t`.
"""

from __future__ import division
from __future__ import absolute_import
from __future__ import print_function
from __future__ import unicode_literals
from future import standard_library
standard_library.install_aliases()

from construct import *  # NOQA: #402
from valvebsp.structs.common import *  # NOQA: #402

dedge_t = Struct(
    'v' / Int16ul[2] * "index into :ref:`lump 3<lump_3>`"
)


@lump_array
@lump_version(0)
def lump_12(header, profile=None):
    return dedge_t

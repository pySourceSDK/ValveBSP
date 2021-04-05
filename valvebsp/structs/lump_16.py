"""
Lump 16 - Leaf Faces
====================

This lump contains an array of :any:`Int<int>`. They are references to face ids in :doc:`lump_7<lump_7>`.
"""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals
from future import standard_library
standard_library.install_aliases()

from construct import *  # NOQA: #402
from valvebsp.structs.common import *  # NOQA: #402


@lump_array
@lump_version(0)
def lump_16(header, profile=None):
    return Int16ul

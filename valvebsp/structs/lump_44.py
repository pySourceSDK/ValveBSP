"""
Lump 44 - Texture Data String Table
===================================

This lump contains an array of :any:`Int<int>`. They represents offsets in :ref:`lump_43<lump_43>`.

Note: Ids pointing to lump 44 should map perfectly to lump 43. It's considered safe to use lump 43 directly instead of 44.
"""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals
from future import standard_library
standard_library.install_aliases()

from construct import *  # NOQA: #402
from valvebsp.structs.common import *  # NOQA #402


@lump_array
@lump_version(0)
def lump_44(header, profile=None):
    return Int32sl

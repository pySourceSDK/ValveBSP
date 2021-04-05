"""
Lump 47 - Face Macro Texture Info
=================================

This lump contains an array of :any:`Int<int>`. They are indices into :doc:`lump_44<lump_44>`.
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
def lump_47(header, profile=None):
    return Int16ul

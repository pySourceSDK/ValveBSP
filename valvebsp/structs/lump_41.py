"""
Lump 41 - Clip Portal Verts
===========================

This lump contains an array of verts represented as :any:`Vector`.
"""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals
from future import standard_library
standard_library.install_aliases()

from valvebsp.structs.common import *  # NOQA: #402


@lump_array
@lump_version(0)
def lump_41(header, profile=None):
    return Vector

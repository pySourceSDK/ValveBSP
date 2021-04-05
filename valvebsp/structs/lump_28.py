"""
Lump 28 - Phys Disp
===================

This lump is not currently implemented. It will return the raw bytes.
"""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals
from future import standard_library
standard_library.install_aliases()

from construct import *  # NOQA: #402
from valvebsp.structs.common import *  # NOQA #402


@lump_raw
@lump_version(0)
def lump_28(header, profile=None):
    return

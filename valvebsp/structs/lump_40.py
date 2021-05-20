"""
Lump 40 - Pakfile
=================

This lump contains raw data. The data can be saved directly to the disc as a zip file.
"""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals
from future import standard_library
standard_library.install_aliases()

from valvebsp.structs.common import *  # NOQA #402


@lump_raw
@lump_version(0)
def lump_40(header, profile=None):
    return

"""
Lump 53 - Lighting HDR
======================

This lump contains an array of :any:`ColorRGBExp32`. They represent individual luxels.
It is the HDR version of :ref:`lump 8<lump_8>`.
"""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals
from future import standard_library
standard_library.install_aliases()

from valvebsp.structs.common import *  # NOQA: #402


@lump_array
@lump_version([0, 1])
def lump_53(header, profile=None):
    return ColorRGBExp32

"""
Lump 58 - Faces HDR
===================

This lump contains an array of :any:`dface_t`. It is the HDR version of :ref:`lump_8<lump_8>`.
"""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals
from future import standard_library
standard_library.install_aliases()

from valvebsp.structs.common import *  # NOQA #402
from valvebsp.structs.lump_7 import dface_t  # NOQA #402


@lump_array
@lump_version([0, 1])
def lump_58(header, profile=None):
    return dface_t

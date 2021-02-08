"""
Lump 58 - Faces HDR
===================

This lump contains an array of :any:`dface_t` (:ref:`as seen in lump_7<lump_7>`).
"""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals
from future import standard_library
standard_library.install_aliases()

from construct import *  # NOQA: #402
from valvebsp.constants import *  # NOQA: #402
from valvebsp.exceptions import *  # NOQA: #402
from valvebsp.structs.common import *  # NOQA #402
from valvebsp.structs.lump_7 import dface_t  # NOQA #402


def lump_58(header, profile=None):
    if header.version in [0, 1]:
        return lump_array(LUMP_FACES_HDR, dface_t, header)
    else:
        raise LumpVersionUnsupportedError(header.version)

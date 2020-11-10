"""
Lump 27 - Original Faces
========================

This lump contains an array of :any:`dface_t` (:ref:`as seen in lump_7<lump_7>`).
"""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals
from future import standard_library
standard_library.install_aliases()

from construct import *  # NOQA: #402
from bsptools.constants import *  # NOQA: #402
from bsptools.exceptions import *  # NOQA: #402
from bsptools.structs.common import *  # NOQA #402
from bsptools.structs.lump_7 import dface_t  # NOQA #402


def lump_27(header, profile=None):
    if header.version != 0:
        raise LumpVersionUnsupportedError(header.version)
    return lump_array(LUMP_ORIGINALFACES, dface_t, header)

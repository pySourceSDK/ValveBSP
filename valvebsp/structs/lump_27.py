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
from valvebsp.structs.common import *  # NOQA #402
from valvebsp.structs.lump_7 import dface_t  # NOQA #402


@lump_array
@lump_version(0)
def lump_27(header, profile=None):
    return dface_t

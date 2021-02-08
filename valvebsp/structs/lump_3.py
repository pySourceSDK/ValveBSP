"""
Lump 3 - Vertexes
=================

This lump contains an array of :any:`Vector`, three floats corresponding to X/Y/Z coordinates. Vertexes are combined to form edges (:ref:`see lump_12<lump_12>`).
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
from valvebsp.structs.common import *  # NOQA: #402


def lump_3(header, profile=None):
    if header.version != 0:
        raise LumpVersionUnsupportedError(header.version)
    return lump_array(LUMP_VERTEXES, Vector, header)

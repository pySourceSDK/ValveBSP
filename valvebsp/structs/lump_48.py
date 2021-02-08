"""
Lump 48 - Disp Tris
===================

This lump contains an array of :any:`CDispTri`.
"""

from __future__ import division
from __future__ import absolute_import
from __future__ import print_function
from __future__ import unicode_literals
from future import standard_library
standard_library.install_aliases()

from construct import *  # NOQA: #402
from valvebsp.constants import *  # NOQA: #402
from valvebsp.exceptions import *  # NOQA: #402
from valvebsp.structs.common import *  # NOQA #402

CDispTri = Struct(
    'tags' / Int16ul
)


def lump_48(header, profile=None):
    if header.version != 0:
        raise LumpVersionUnsupportedError(header.version)
    return lump_array(LUMP_DISP_TRIS, CDispTri, header)

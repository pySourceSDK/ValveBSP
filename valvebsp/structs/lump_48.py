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
from valvebsp.structs.common import *  # NOQA #402

CDispTri = Struct(
    'tags' / Int16ul
)


@lump_array
@lump_version(0)
def lump_48(header, profile=None):
    return CDispTri

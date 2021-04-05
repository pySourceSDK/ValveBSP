"""
Lump 33 - Disp Verts
====================

This lump contains an array of :any:`CDispVert`.
"""

from __future__ import division
from __future__ import absolute_import
from __future__ import print_function
from __future__ import unicode_literals
from future import standard_library
standard_library.install_aliases()

from construct import *  # NOQA: #402
from valvebsp.structs.common import *  # NOQA #402

CDispVert = Struct(
    'vector' / Vector,
    'dist' / Float32l,
    'alpha' / Float32l,
)


@lump_array
@lump_version(0)
def lump_33(header, profile=None):
    return CDispVert

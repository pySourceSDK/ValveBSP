"""
Lump 6 - Texture Info
=====================

This lump contains an array of :any:`texinfo_t`.
"""

from __future__ import division
from __future__ import absolute_import
from __future__ import print_function
from __future__ import unicode_literals
from future import standard_library
standard_library.install_aliases()

from construct import *  # NOQA: #402
from valvebsp.structs.common import *  # NOQA: #402
from valvebsp.structs.flags import texinfo_flags32  # NOQA: #402

texinfo_t = Struct(
    'textureVecsTexelsPerWorldUnits' / Float32l[2][4],
    'lightmapVecsLuxelsPerWorldUnits' / Float32l[2][4],
    'flags' / texinfo_flags32,
    'texData' / Int32sl * 'index into :ref:`lump 2<lump_2>`',
)


@lump_array
@lump_version(0)
def lump_6(header, profile=None):
    return texinfo_t

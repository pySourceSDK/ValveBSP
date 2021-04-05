"""
Lump 36 - Leaf Water Data
=========================

This lump contains an array of :any:`dleafwaterdata_t`.
"""

from __future__ import division
from __future__ import absolute_import
from __future__ import print_function
from __future__ import unicode_literals
from future import standard_library
standard_library.install_aliases()

from construct import *  # NOQA: #402
from valvebsp.structs.common import *  # NOQA #402

dleafwaterdata_t = Aligned(4, Struct(
    'surfaceZ' / Float32l,
    'minZ' / Float32l,
    'surfaceTexInfoID' / Int16sl,
))


@lump_array
@lump_version(0)
def lump_36(header, profile=None):
    return dleafwaterdata_t

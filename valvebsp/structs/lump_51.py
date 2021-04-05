"""
Lump 51 - Lightmap Pages ...or Leaf Ambient Index HDR
=====================================================

This lump contains an array of :any:`dleafambientindex_t`.
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
from valvebsp.structs.common import *  # NOQA: #402

dleafambientindex_t = Struct(  # matches dleaf_t
    'ambientSampleCount' / Int16ul,
    'firstAmbientSample' / Int16ul
)


@lump_array
def lump_51(header, profile=None):
    if header.version == 0:
        return dleafambientindex_t
    elif header.version == 1:
        return dleafambientindex_t
    else:
        raise LumpVersionUnsupportedError(header.version)

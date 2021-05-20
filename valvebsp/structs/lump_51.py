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
from valvebsp.structs.common import *  # NOQA: #402

dleafambientindex_t = Struct(  # matches dleaf_t
    'ambientSampleCount' / Int16ul,
    'firstAmbientSample' / Int16ul * \
    "index into :ref:`lump 55<lump_55>` or :ref:`lump 56<lump_56>`",
)


@lump_array
@lump_version([0, 1])
def lump_51(header, profile=None):
    return dleafambientindex_t

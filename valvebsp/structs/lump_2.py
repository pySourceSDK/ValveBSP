
"""
Lump 2 - Texture Data
=====================

This lump contains an array of :any:`dtexdata_t`.
"""

from __future__ import division
from __future__ import absolute_import
from __future__ import print_function
from __future__ import unicode_literals
from future import standard_library
standard_library.install_aliases()

from construct import *  # NOQA: #402
from valvebsp.structs.common import *  # NOQA: #402

dtexdata_t = Struct(
    'reflectivity' / Vector * "RGB reflectivity",
    'nameStringTableID' / Int32sl * "index into :ref:`lump 44<lump_44>`",
    'width' / Int32sl,
    'height' / Int32sl,
    'viewWidth' / Int32sl,
    'viewHeight' / Int32sl
)


@lump_array
@lump_version(0)
def lump_2(header, profile=None):
    return dtexdata_t

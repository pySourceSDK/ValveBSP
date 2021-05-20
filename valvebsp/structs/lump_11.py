"""
Lump 11 - Face Ids
==================

This lump contains an array of :any:`dfaceid_t`. This array matches the array of dface_t (:ref:`see lump_7<lump_7>`).
"""

from __future__ import division
from __future__ import absolute_import
from __future__ import print_function
from __future__ import unicode_literals
from future import standard_library
standard_library.install_aliases()

from construct import *  # NOQA: #402
from valvebsp.structs.common import *  # NOQA: #402

dfaceid_t = Struct(
    'hammerFaceID' / Int16ul * "index into :ref:`lump 27<lump_27>`",
)


@lump_array
@lump_version(0)
def lump_11(header, profile=None):
    return dfaceid_t

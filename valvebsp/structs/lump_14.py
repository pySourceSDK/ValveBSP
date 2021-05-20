"""
Lump 14 - Models
================

This lump contains an array of :any:`dmodel_t`.
"""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals
from future import standard_library
standard_library.install_aliases()

from construct import *  # NOQA: #402
from valvebsp.structs.common import *  # NOQA: #402


dmodel_t = Struct(
    'mins' / Vector * 'lower point of the bounding box',
    'maxs' / Vector * 'higher point the bounding box',
    'origin' / Vector,
    'headnode' / Int32sl * 'index into :ref:`lump 5<lump_5>`',
    'firstface' / Int32sl * 'index into :ref:`lump 7<lump_7>`',
    'numfaces' / Int32sl
)


@lump_array
@lump_version(0)
def lump_14(header, profile=None):
    return dmodel_t

"""
Lump 19 - Brush Sides
=====================

This lump contains an array of :any:`dbrushside_t`.

Note: Portal 2's implementation of this lump differs, a :ref:`profile<profiles>` must be specified.
"""

from __future__ import division
from __future__ import absolute_import
from __future__ import print_function
from __future__ import unicode_literals
from future import standard_library
standard_library.install_aliases()

from construct import *  # NOQA: #402
from valvebsp.structs.common import *  # NOQA: #402

dbrushside_t_P2 = Struct(
    'planeNum' / Int16ul,
    'texInfo' / Int16sl * "index into :ref:`lump 6<lump_6>`",
    'dispInfo' / Int16sl * "index into :ref:`lump 26<lump_26>`",
    'bevel' / Int8sl,
    'thin' / Int8sl
)

dbrushside_t = Struct(
    'planeNum' / Int16ul,
    'texInfo' / Int16sl * "index into :ref:`lump 6<lump_6>`",
    'dispInfo' / Int16sl * "index into :ref:`lump 26<lump_26>`",
    'bevel' / Int16sl
)


@lump_array
@lump_version(0)
def lump_19(header, profile=None):
    if profile in [ALIENSWARM, PORTAL2]:
        return dbrushside_t_P2
    else:
        return dbrushside_t

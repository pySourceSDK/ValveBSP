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
from valvebsp.constants import *  # NOQA: #402
from valvebsp.exceptions import *  # NOQA: #402
from valvebsp.structs.common import *  # NOQA: #402

dbrushside_t_P2 = Struct(
    'planeNum' / Int16ul,
    'texInfo' / Int16sl,
    'dispInfo' / Int16sl,
    'bevel' / Int8sl,
    'thin' / Int8sl
)

dbrushside_t = Struct(
    'planeNum' / Int16ul,
    'texInfo' / Int16sl,
    'dispInfo' / Int16sl,
    'bevel' / Int16sl
)


def lump_19(header, profile=None):
    if header.version == 0:
        if profile in [ALIENSWARM, PORTAL2]:
            return lump_array(LUMP_BRUSHSIDES, dbrushside_t_P2, header)
        else:
            return lump_array(LUMP_BRUSHSIDES, dbrushside_t, header)
    else:
        raise LumpVersionUnsupportedError(header.version)

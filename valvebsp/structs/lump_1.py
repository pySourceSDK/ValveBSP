"""
Lump 1 - Planes
===============

This lump contains an array of :any:`dplane_t`.
"""

from __future__ import division
from __future__ import absolute_import
from __future__ import print_function
from __future__ import unicode_literals
from future import standard_library
standard_library.install_aliases()

from construct import Struct, Int32sl, Float32l, Padding  # NOQA: #402
from valvebsp.constants import LUMP_PLANES  # NOQA: #402
from valvebsp.exceptions import LumpVersionUnsupportedError  # NOQA: #402
from valvebsp.structs.common import Vector, lump_array  # NOQA: #402


dplane_t = Struct(
    'normal' / Vector,
    'dist' / Float32l,
    'type' / Int32sl
)


def lump_1(header, profile=None):
    if header.version != 0:
        raise LumpVersionUnsupportedError(header.version)
    return lump_array(LUMP_PLANES, dplane_t, header)

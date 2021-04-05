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

from construct import Struct, Int32sl, Float32l  # NOQA: #402
from valvebsp.structs.common import *  # NOQA: #402


dplane_t = Struct(
    'normal' / Vector,
    'dist' / Float32l,
    'type' / Int32sl
)


@lump_array
@lump_version(0)
def lump_1(header, profile=None):
    return dplane_t

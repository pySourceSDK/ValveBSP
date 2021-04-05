"""
Lump 60 - Overlay Fades
=======================

This lump contains an array of :any:`doverlayfade_t`.
"""

from __future__ import division
from __future__ import absolute_import
from __future__ import print_function
from __future__ import unicode_literals
from future import standard_library
standard_library.install_aliases()

from construct import *  # NOQA: #402
from valvebsp.structs.common import *  # NOQA #402


doverlayfade_t = Struct(
    'fadeDistMinSq' / Float32l,
    'fadeDistMaxSq' / Float32l
)


@lump_array
@lump_version(0)
def lump_60(header, profile=None):
    return doverlayfade_t

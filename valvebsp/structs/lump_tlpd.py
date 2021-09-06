"""
Lump tlpd - Prop Detail Lighting
================================

This lump contains an array of :any:`DetailPropLightStyle_t`.
In bsp, this array is prefixed by an integer representing its length.
"""

from __future__ import division
from __future__ import absolute_import
from __future__ import print_function
from __future__ import unicode_literals
from __future__ import division
from future import standard_library
standard_library.install_aliases()

from construct import *  # NOQA: #402
from valvebsp.structs.common import *  # NOQA: #402

DetailPropLightStyle_t = Struct(
    'lighting' / ColorRGBExp32,
    'style' / Int8ul,
)


@lump_version(0)
@lump_prefixed_array(Int32sl)
def lump_tlpd(header, profile=None):
    return DetailPropLightStyle_t

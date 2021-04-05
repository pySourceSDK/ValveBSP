"""
Lump tlpd - Prop Detail Lighting
================================

This lump is defined as a single :any:`DetailPropLightStylesLump_t`
"""

from __future__ import division
from __future__ import absolute_import
from __future__ import print_function
from __future__ import unicode_literals
from future import standard_library
standard_library.install_aliases()

from construct import *  # NOQA: #402
from valvebsp.structs.common import *  # NOQA: #402

DetailPropLightStyleLump_t = Struct(
    'lighting' / ColorRGBExp32,
    'style' / Int8ul,
)

DetailPropLightStylesLump_t = Struct(
    'count' / Int32sl,
    'styles' / DetailPropLightStyleLump_t[this.count]
)


@lump_struct
@lump_version(0)
def lump_tlpd(header, profile=None):
    return DetailPropLightStylesLump_t

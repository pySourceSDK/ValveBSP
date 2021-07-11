"""
Lump prpd - Prop Detail
=======================

This lump is defined as a single :any:`DetailPropLump_t`
"""

from __future__ import division
from __future__ import absolute_import
from __future__ import print_function
from __future__ import unicode_literals
from future import standard_library
standard_library.install_aliases()

from construct import *  # NOQA: #402
from valvebsp.structs.common import *  # NOQA: #402

DetailPropOrientation_t = Enum(
    Int8ul,
    DETAIL_PROP_ORIENT_NORMAL=0,
    DETAIL_PROP_ORIENT_SCREEN_ALIGNED=1,
    DETAIL_PROP_ORIENT_SCREEN_ALIGNED_VERTICAL=2,
)

DetailPropType_t = Enum(
    Int8ul,
    DETAIL_PROP_TYPE_MODEL=0,
    DETAIL_PROP_TYPE_SPRITE=1,
    DETAIL_PROP_TYPE_SHAPE_CROSS=2,
    DETAIL_PROP_TYPE_SHAPE_TRI=3,
)

DetailSpriteLump_t = Struct(
    'UL' / Vector2D,
    'LR' / Vector2D,
    'texUL' / Vector2D,
    'texLR' / Vector2D,
)

DetailObjectLump_t = Struct(
    'origin' / Vector,
    'angles' / QAngle,
    'detailModel' / Int16ul,
    'leaf' / Int16ul,
    'lighting' / ColorRGBExp32,
    'lightStyles' / Int32sl,
    'lightStyleCount' / Int8ul,
    'swayAmount' / Int8ul,
    'shapeAngle' / Int8ul,
    'shapeSize' / Int8ul,
    'orientation' / DetailPropOrientation_t,
    'padding2' / Int8ul[3],
    'type' / DetailPropType_t,
    'padding3' / Int8ul[3],
    'scale' / Float32l
)

DetailPropLump_t = Struct(
    'dictLump' / PrefixedArray(Int32sl,
                               PaddedString(DETAIL_NAME_LENGTH, 'ascii')),
    'spritesLump' / PrefixedArray(Int32sl, DetailSpriteLump_t),
    'objectLump' / PrefixedArray(Int32sl, DetailObjectLump_t)
)


@lump_struct
@lump_version(4)
def lump_prpd(header, profile=None):
    return DetailPropLump_t

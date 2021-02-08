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
from valvebsp.constants import *  # NOQA: #402
from valvebsp.exceptions import *  # NOQA: #402
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

DetailPropDictLump_t = Struct(
    'count' / Int32sl,
    'names' / PaddedString(DETAIL_NAME_LENGTH, 'ascii')[this.count]
)

DetailSpriteDictLump_t = Struct(
    'count' / Int32sl,
    'sprites' / DetailSpriteLump_t[this.count]
)

DetailObjectDictLump_t = Struct(
    'count' / Int32sl,
    'objects' / DetailObjectLump_t[this.count]
)

DetailPropLump_t = Struct(
    'dictLump' / DetailPropDictLump_t,
    'spritesLump' / DetailSpriteDictLump_t,
    'objectLump' / DetailObjectDictLump_t
)


def lump_prpd(header, profile=None):
    if header.version != 4:
        raise LumpVersionUnsupportedError(header.version)

    return lump_game('prpd', DetailPropLump_t, header)

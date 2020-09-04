from __future__ import division
from __future__ import absolute_import
from __future__ import print_function
from __future__ import unicode_literals
from future import standard_library
standard_library.install_aliases()

from construct import *  # NOQA: #402
from bsptools.constants import *  # NOQA: #402
from bsptools.exceptions import *  # NOQA: #402
from bsptools.structs.common_struct import *  # NOQA: #402

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
    'm_UL' / Vector2D,
    'm_LR' / Vector2D,
    'm_TexUL' / Vector2D,
    'm_TexLR' / Vector2D,
)

DetailObjectLump_t = Struct(
    'm_Origin' / Vector,
    'm_Angles' / QAngle,
    'm_DetailModel' / Int16ul,
    'm_Leaf' / Int16ul,
    'm_Lighting' / ColorRGBExp32,
    'm_LightStyles' / Int32sl,
    'm_LightStyleCount' / Int8ul,
    'm_SwayAmount' / Int8ul,
    'm_ShapeAngle' / Int8ul,
    'm_ShapeSize' / Int8ul,
    'm_Orientation' / DetailPropOrientation_t,
    'm_Padding2' / Int8ul[3],
    'm_Type' / DetailPropType_t,
    'm_Padding3' / Int8ul[3],
    'm_flScale' / Float32l
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
    'dict_lump' / DetailPropDictLump_t,
    'sprites_lump' / DetailSpriteDictLump_t,
    'objects_lump' / DetailObjectDictLump_t
)


def lump_prpd(version):
    if version != 4:
        raise LumpVersionUnsupportedError(version)

    return lump_game('prpd', DetailPropLump_t)

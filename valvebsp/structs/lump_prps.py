"""
Lump prps - Prop Static
=======================

This lump is defined as a single StaticPropLump_t that may come in different versions, in accordance with the gamelump.`
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

prps_flags8 = FlagsEnum(Int8ul,
                        STATIC_PROP_FLAG_FADES=1,
                        STATIC_PROP_USE_LIGHTING_ORIGIN=2,
                        STATIC_PROP_NO_DRAW=4,
                        STATIC_PROP_IGNORE_NORMALS=8,
                        STATIC_PROP_NO_SHADOW=16,
                        STATIC_PROP_SCREEN_SPACE_FADE_OBSOLETE=32,
                        STATIC_PROP_NO_PER_VERTEX_LIGHTING=64,
                        STATIC_PROP_NO_SELF_SHADOWING=128)

StaticPropV4_t = Struct(
    'origin' / Vector,
    'angles' / QAngle,

    'propType' / Int16ul * 'refers to prps.dict_lump',
    'firstLeaf' / Int16ul * 'refers to prps.leaf_lump',
    'leafCount' / Int16ul,
    'solid' / Int8ul,
    'flags' / prps_flags8,
    'skin' / Int32sl,

    'fadeMinDist' / Float32l,
    'fadeMaxDist' / Float32l,

    'lightingOrigin' / Vector,
)

StaticPropV5_t = Struct(
    # hl, hl2, p1, css
    'origin' / Vector,
    'angles' / QAngle,

    'propType' / Int16ul * 'refers to prps.dict_lump',
    'firstLeaf' / Int16ul * 'refers to prps.leaf_lump',
    'leafCount' / Int16ul,
    'solid' / Int8ul,
    'flags' / prps_flags8,
    'skin' / Int32sl,

    'fadeMinDist' / Float32l,
    'fadeMaxDist' / Float32l,

    'lightingOrigin' / Vector,
    'forcedFadeScale' / Float32l,
)

StaticPropV6_t = Struct(
    # p1, css, dod
    'origin' / Vector,
    'angles' / QAngle,

    'propType' / Int16ul * 'refers to prps.dict_lump',
    'firstLeaf' / Int16ul * 'refers to prps.leaf_lump',
    'leafCount' / Int16ul,
    'solid' / Int8ul,
    'flags' / prps_flags8,
    'skin' / Int32sl,

    'FadeMinDist' / Float32l,
    'FadeMaxDist' / Float32l,

    'lightingOrigin' / Vector,
    'forcedFadeScale' / Float32l,

    'minDXLevel' / Int16ul,
    'maxDXLevel' / Int16ul,
)

StaticPropV7_t = Struct(
    # zeno
    'origin' / Vector,
    'angles' / QAngle,

    'propType' / Int16ul * 'refers to prps.dict_lump',
    'firstLeaf' / Int16ul * 'refers to prps.leaf_lump',
    'leafCount' / Int16ul,
    'solid' / Int8ul,
    'flags' / prps_flags8,
    'skin' / Int32sl,

    'FadeMinDist' / Float32l,
    'FadeMaxDist' / Float32l,

    'lightingOrigin' / Vector,
    'forcedFadeScale' / Float32l,

    'minDXLevel' / Int16ul,
    'maxDXLevel' / Int16ul,

    'diffuseModulation' / color32,
)

StaticPropV8_t = Struct(
    'origin' / Vector,
    'angles' / QAngle,

    'propType' / Int16ul * 'refers to prps.dict_lump',
    'firstLeaf' / Int16ul * 'refers to prps.leaf_lump',
    'leafCount' / Int16ul,
    'solid' / Int8ul,
    'flags' / prps_flags8,
    'skin' / Int32sl,

    'FadeMinDist' / Float32l,
    'FadeMaxDist' / Float32l,

    'lightingOrigin' / Vector,
    'forcedFadeScale' / Float32l,

    'minCPULevel' / Int8ul,
    'maxCPULevel' / Int8ul,
    'minGPULevel' / Int8ul,
    'maxGPULevel' / Int8ul,

    'diffuseModulation' / color32,
)


StaticPropV9_t = Struct(
    # portal2
    'origin' / Vector,
    'angles' / QAngle,

    'propType' / Int16ul * 'refers to prps.dict_lump',
    'firstLeaf' / Int16ul * 'refers to prps.leaf_lump',
    'leafCount' / Int16ul,
    'solid' / Int8ul,
    'flags' / prps_flags8,
    'skin' / Int32sl,

    'FadeMinDist' / Float32l,
    'FadeMaxDist' / Float32l,

    'lightingOrigin' / Vector,
    'forcedFadeScale' / Float32l,

    'minCPULevel' / Int8ul,
    'maxCPULevel' / Int8ul,
    'minGPULevel' / Int8ul,
    'maxGPULevel' / Int8ul,

    'diffuseModulation' / color32,

    'disableX360' / Aligned(4, Flag)
)


StaticPropV10_t = Aligned(4, Struct(
    # tf2
    'origin' / Vector,
    'angles' / QAngle,

    'propType' / Int16ul * 'refers to prps.dict_lump',
    'firstLeaf' / Int16ul * 'refers to prps.leaf_lump',
    'leafCount' / Int16ul,

    'solid' / Int8ul,
    'flags' / prps_flags8,
    'skin' / Int32sl,

    'FadeMinDist' / Float32l,
    'FadeMaxDist' / Float32l,

    'lightingOrigin' / Vector,
    'forcedFadeScale' / Float32l,

    'minCPULevel' / Int8ul,
    'maxCPULevel' / Int8ul,
    'minGPULevel' / Int8ul,
    'maxGPULevel' / Int8ul,

    'diffuseModulation' / color32,

    'flagEx' / Int32ul,
))

StaticPropV11_t = Aligned(4, Struct(
    # csgo
    'origin' / Vector,
    'angles' / QAngle,

    'propType' / Int16ul * 'refers to prps.dict_lump',
    'firstLeaf' / Int16ul * 'refers to prps.leaf_lump',
    'leafCount' / Int16ul,

    'solid' / Int8ul,
    'flags' / prps_flags8,
    'skin' / Int32sl,

    'FadeMinDist' / Float32l,
    'FadeMaxDist' / Float32l,

    'lightingOrigin' / Vector,
    'forcedFadeScale' / Float32l,

    'minCPULevel' / Int8ul,
    'maxCPULevel' / Int8ul,
    'minGPULevel' / Int8ul,
    'maxGPULevel' / Int8ul,

    'diffuseModulation' / color32,

    'disableX360' / Aligned(4, Flag),

    'flagsEx' / Int32ul,

    'uniformScale' / Float32l,
))


StaticPropDictLump_t = Struct(
    'count' / Int32sl,
    'names' / PaddedString(STATIC_PROP_NAME_LENGTH, 'ascii')[this.count]
)
StaticPropLeafDictLump_t = Struct(
    'count' / Int32sl,
    'leafs' / Int16ul[this.count]
)
StaticPropLightstylesDictLump_t = Struct(
    'count' / Int32sl,
    'lightstyles' / ColorRGBExp32[this.count]
)


def lump_prps(header, profile=None):
    if header.version == 11:
        StaticProp_t = StaticPropV11_t
    elif header.version == 10:
        StaticProp_t = StaticPropV10_t
    elif header.version == 9:
        StaticProp_t = StaticPropV9_t
    elif header.version == 8:
        StaticProp_t = StaticPropV8_t
    elif header.version == 7:
        StaticProp_t = StaticPropV7_t
    elif header.version == 6:
        StaticProp_t = StaticPropV6_t
    elif header.version == 5:
        StaticProp_t = StaticPropV5_t
    elif header.version == 4:
        StaticProp_t = StaticPropV4_t
    else:
        raise LumpVersionUnsupportedError(header.version)

    if profile == ZENOCLASH:
        StaticPropLump_t = Struct(
            'dictLump' / StaticPropDictLump_t,
            'dictLump2' / StaticPropDictLump_t,
            'leafLump' / StaticPropLeafDictLump_t,
            'objectLump' / Struct('count' / Int32sl,
                                  'objects' / Aligned(4, StaticProp_t[this.count])),
            'lightstylesLump' / StaticPropLightstylesDictLump_t)
    else:
        StaticPropLump_t = Struct(
            'dictLump' / StaticPropDictLump_t,
            'leafLump' / StaticPropLeafDictLump_t,
            'objectLump' / Struct('count' / Int32sl,
                                  'objects' / Aligned(4, StaticProp_t[this.count])),
            'lightstylesLump' / StaticPropLightstylesDictLump_t)

    return lump_game('prps', StaticPropLump_t, header)

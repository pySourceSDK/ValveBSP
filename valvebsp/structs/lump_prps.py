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
from valvebsp.structs.common import *  # NOQA: #402
from valvebsp.structs.flags import prps_flags8  # NOQA: #402


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

    'flagsEx' / Int32ul,
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


@lump_version([4, 5, 6, 7, 8, 9, 10, 11])
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

    if profile == ZENOCLASH:
        StaticPropLump_t = Struct(
            'dictLump' / PrefixedArray(Int32sl, PaddedString(
                STATIC_PROP_NAME_LENGTH, 'ascii')),
            'dictLump2' / PrefixedArray(Int32sl, PaddedString(
                STATIC_PROP_NAME_LENGTH, 'ascii')),
            'leafLump' / PrefixedArray(Int32sl, Int16ul),
            'objectLump' / PrefixedArray(Int32sl, StaticProp_t))
    else:
        StaticPropLump_t = Struct(
            'dictLump' / PrefixedArray(Int32sl, PaddedString(
                STATIC_PROP_NAME_LENGTH, 'ascii')),
            'leafLump' / PrefixedArray(Int32sl, Int16ul),
            'objectLump' / PrefixedArray(Int32sl, StaticProp_t))

    return StaticPropLump_t

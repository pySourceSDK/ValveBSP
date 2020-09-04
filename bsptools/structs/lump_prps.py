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

StaticPropV4_t = Struct(
    'Origin' / Vector,
    'Angles' / QAngle,

    'PropType' / Int16ul,
    'FirstLeaf' / Int16ul,
    'm_LeafCount' / Int16ul,

    'Solid' / Int8ul,
    'Flags' / Int8ul,
    'Skin' / Int32sl,

    'FadeMinDist' / Float32l,
    'FadeMaxDist' / Float32l,

    'LightingOrigin' / Vector,

    'MinDXLevel' / Int16ul,
    'MaxDXLevel' / Int16ul,
)

StaticPropV5_t = Struct(
    'm_Origin' / Vector,
    'm_Angles' / QAngle,

    'm_PropType' / Int16ul,
    'm_FirstLeaf' / Int16ul,
    'm_LeafCount' / Int16ul,

    'm_Solid' / Int8ul,
    'm_Flags' / Int8ul,
    'm_Skin' / Int32sl,

    'm_FadeMinDist' / Float32l,
    'm_FadeMaxDist' / Float32l,

    'm_LightingOrigin' / Vector,

    'm_nMinDXLevel' / Int16ul,
    'm_nMaxDXLevel' / Int16ul,
)

StaticPropV6_t = Struct(
    'Origin' / Vector,
    'Angles' / QAngle,

    'PropType' / Int16ul,
    'FirstLeaf' / Int16ul,
    'LeafCount' / Int16ul,

    'Solid' / Int8ul,
    'Flags' / Int32ul,
    'Skin' / Int32sl,

    'FadeMinDist' / Float32l,
    'FadeMaxDist' / Float32l,

    'LightingOrigin' / Vector,

    'MinDXLevel' / Int16ul,
    'MaxDXLevel' / Int16ul,
)

StaticPropV8_t = Struct(
    'Origin' / Vector,
    'Angles' / QAngle,

    'PropType' / Int16ul,
    'FirstLeaf' / Int16ul,
    'LeafCount' / Int16ul,

    'Solid' / Int8ul,
    'Flags' / Int8ul,
    'Skin' / Int32sl,

    'FadeMinDist' / Float32l,
    'FadeMaxDist' / Float32l,

    'LightingOrigin' / Vector,

    'ForcedFadeScale' / Float32l,

    'MinCPULevel' / Int8ul,
    'MaxCPULevel' / Int8ul,
    'MinGPULevel' / Int8ul,
    'MaxGPULevel' / Int8ul,

    'DiffuseModulation' / color32,
)

StaticPropV10_t = Struct(
    'Origin' / Vector,
    'Angles' / QAngle,

    'PropType' / Int16ul,
    'FirstLeaf' / Int16ul,
    'LeafCount' / Int16ul,

    'Solid' / Int8ul,
    'Flags' / Int32ul,
    'Skin' / Int32sl,

    'FadeMinDist' / Float32l,
    'FadeMaxDist' / Float32l,

    'LightingOrigin' / Vector,

    'ForcedFadeScale' / Float32l,

    'MinCPULevel' / Int8ul,
    'MaxCPULevel' / Int8ul,
    'MinGPULevel' / Int8ul,
    'MaxGPULevel' / Int8ul,

    'DiffuseModulation' / color32,

    'DisableX360' / Int8ul,

    #'m_nLightmapResolutionX' / Int16ul,
    #'m_nLightmapResolutionY' / Int16ul,
    #'dirt' / Int8ul
)


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


def lump_prps(version):
    # hl2ep2 is version 4
    # l4d is version 8

    if version == 10:
        StaticProp_t = StaticPropV10_t
    elif version == 8:
        StaticProp_t = StaticPropV8_t
    elif version == 6:
        StaticProp_t = StaticPropV6_t
    elif version == 4:
        StaticProp_t = StaticPropV4_t
    else:
        raise LumpVersionUnsupportedError(version)

    StaticPropLump_t = Struct(
        'dict_lump' / StaticPropDictLump_t,
        'leaf_lump' / StaticPropLeafDictLump_t,
        'object_lump' / Struct('count' / Int32sl,
                               'objects' / Aligned(4, StaticProp_t[this.count])),
        'lightstyles_lump' / StaticPropLightstylesDictLump_t
    )

    return lump_game('prps', StaticPropLump_t)

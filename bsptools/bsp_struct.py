from __future__ import division
from __future__ import absolute_import
from __future__ import unicode_literals
from __future__ import print_function
from builtins import int
from future import standard_library
standard_library.install_aliases()


from construct import *	 # NOQA: #402
from .constants import *  # NOQA: #402
from .common_struct import *  # NOQA: #402

lump_t = Struct(
    'fileofs' / Int32sl,
    'filelen' / Int32sl,
    'version' / Int32sl,
    'uncompressedSize' / Int32sl
)

dplane_t = Struct(
    'normal' / Vector,
    'dist' / Float32l,
    'type' / Int32sl
)

dtexdata_t = Struct(
    'reflectivity' / Vector,  # RGB reflectivity
    'nameStringTableID' / Int32sl,  # index into TexdataStringTable
    'width' / Int32sl,
    'height' / Int32sl,
    'view_width' / Int32sl,
    'view_height' / Int32sl
)

dvis_t = Struct(
    'numclusters' / Int32sl,
    'bitofs' / Int32sl[8][2]
)

dnode_t = Aligned(4, Struct(
    'planenum' / Int32sl,
    'children' / Int32sl[2],
    'mins' / Int16sl[3],
    'maxs' / Int16sl[3],
    'firstface' / Int16ul,
    'numfaces' / Int16ul,
    'area' / Int16sl,
))

texinfo_t = Struct(
    'textureVecsTexelsPerWorldUnits' / Float32l[2][4],
    'lightmapVecsLuxelsPerWorldUnits' / Float32l[2][4],
    'flags' / Int32sl,
    'texdata' / Int32sl,
)

dface_t = Struct(
    'planenum' / Int16ul,
    'side' / Byte,
    'onNode' / Byte,
    'firstedge' / Int32sl,
    'numedges' / Int16sl,
    'texinfo' / Int16sl,
    'dispinfo' / Int16sl,
    'surfaceFogVolumeID' / Int16sl,
    'styles' / Byte[4],
    'lightofs' / Int32sl,
    'area' / Float32l,
    'LightmapTextureMinsInLuxels' / Int32sl[2],
    'LightmapTextureSizeInLuxels' / Int32sl[2],
    'origFace' / Int32sl,
    'numPrims' / Int16ul,
    'firstPrimID' / Int16ul,
    'smoothingGroups' / Int32ul,
)

ColorRGBExp32 = Struct(
    'r' / Byte,
    'g' / Byte,
    'b' / Byte,
    'exponent' / Byte
)

CompressedLightCube = Struct(
    'm_color' / ColorRGBExp32[6]
)

doccluderdata_t = Struct(
    'flags' / Int32sl,
    'firstpoly' / Int32sl,
    'polycount' / Int32sl,
    'mins' / Vector,
    'maxs' / Vector,
    'area' / Int32sl,
)

doccluderpolydata_t = Struct(
    'firstvertexindex' / Int32sl,
    'vertexcount' / Int32sl,
    'planenum' / Int32sl,
)

doccluder_t = Struct(
    'count' / Int32sl,
    'data' / doccluderdata_t[this.count],
    'polyDataCount' / Int32sl,
    'polyData' / doccluderpolydata_t[this.polyDataCount],
    'vertexIndexCount' / Int32sl,
    'vertexIndices' / Int32sl[this.vertexIndexCount],
)

dfaceid_t = Struct(
    'hammerfaceid' / Int16ul
)

dedge_t = Struct(
    'v' / Int16ul[2]
)

emittype_t = Enum(
    Int32sl,
    emit_surface=0,
    emit_point=1,
    emit_spotlight=2,
    emit_skylight=3,
    emit_quakelight=4,
    emit_skyambient=5
)

dworldlight_t = Struct(
    'origin' / Vector,
    'intensity' / Vector,
    'normal' / Vector,
    'cluster' / Int32sl,
    'type' / emittype_t,
    'style' / Int32sl,
    'stopdot' / Float32l,
    'stopdot2' / Float32l,
    'exponent' / Float32l,
    'radius' / Float32l,
    'constant_attn' / Float32l,
    'linear_attn' / Float32l,
    'quadratic_attn' / Float32l,
    'flags' / Int32sl,
    'texinfo' / Int32sl * "refers to lump 2",
    'owner' / Int32sl,  # lump 0
)

dbrush_t = Struct(
    'firstside' / Int32sl,
    'numsides' / Int32sl,
    'contents' / Int32sl,
)

dbrushside_t = Struct(
    'planenum' / Int32ul,
    'texinfo' / Int32sl,
    'dispinfo' / Int32sl,
    'bevel' / Int32sl
)

darea_t = Struct(
    'numareaportals' / Int32sl,
    'firstareaportal' / Int32sl
)

dareaportal_t = Struct(
    'm_PortalKey' / Int16ul,
    'otherarea' / Int16ul,
    'm_FirstClipPortalVert' / Int16ul,
    'm_nClipPortalVerts' / Int16ul,
    'planenum' / Int32sl
)

dleaf_t = Struct(
    'contents' / Int32sl,
    'cluster' / Int16sl,


    'areaflag' / BitStruct(
        'area' / BitsInteger(7),
        'flags' / BitsInteger(9)),
    'unknown' / Int16sl,

    'mins' / Int16sl[3],
    'maxs' / Int16sl[3],

    'firstleafface' / Int16ul,
    'numleaffaces' / Int16ul,

    'firstleafbrush' / Int16ul,
    'numleafbrushes' / Int16ul,
    'leafWaterDataID' / Int16sl
)

dleafambientlighting_t = Aligned(4, Struct(
    'cube' / CompressedLightCube,
    'x' / Byte,
    'y' / Byte,
    'z' / Byte
))

dleafambientindex_t = Struct(  # matches dleaf_t
    'ambientSampleCount' / Int16ul,
    'firstAmbientSample' / Int16ul
)

dleafwaterdata_t = Aligned(4, Struct(
    'surfaceZ' / Float32l,
    'minZ' / Float32l,
    'surfaceTexInfoID' / Int16sl,
))

dcubemapsample_t = Struct(
    'origin' / Int32sl[3],
    'size' / Int32sl
)

dflagslump_t = Struct(
    'mLevelFalgs' / Int32ul,
)

doverlay_t = Struct(
    'nId' / Int32sl,
    'nTexInfo' / Int16sl,
    'm_nFaceCountAndRenderOrder' / Int16ul,
    'aFaces' / Int32sl[OVERLAY_BSP_FACE_COUNT],
    'flU' / Float32l[2],
    'flV' / Float32l[2],
    'vecUVPoints' / Vector[4],
    'vecOrigin' / Vector,
    'vecBasisNormal' / Vector
)

dwateroverlay_t = Struct(
    'nId' / Int32sl,
    'nTexInfo' / Int16sl,
    'm_nFaceCountAndRenderOrder' / Int16ul,
    'aFaces' / Int32sl[OVERLAY_BSP_FACE_COUNT],
    'flU' / Float32l[2],
    'flV' / Float32l[2],
    'vecUVPoints' / Vector[4],
    'vecOrigin' / Vector,
    'vecBasisNormal' / Vector
)

doverlayfade_t = Struct(
    'flFadeDistMinSq' / Float32l,
    'flFadeDistMaxSq' / Float32l
)

NeighborSpan = Enum(
    Int8sl,
    CORNER_TO_CORNER=0,
    CORNER_TO_MIDPOINT=1,
    MIDPOINT_TO_CORNER=2
)

NeighborOrientation = Enum(
    Int8sl,
    ORIENTATION_CCW_0=0,
    ORIENTATION_CCW_90=1,
    ORIENTATION_CCW_180=2,
    ORIENTATION_CCW_270=3
)


CDispSubNeighbor = Struct(
    # 'm_iNeighbor' / Int16ul,
    # 'm_NeighborOrientation' / NeighborOrientation,
    # 'm_Span' / NeighborSpan,
    # 'm_NeighborSpan' / NeighborSpan
    # The fields seem to be misordered, this is my best guess
    'm_Span' / NeighborSpan,
    'm_NeighborSpan' / NeighborSpan,
    'm_iNeighbor' / Int16ul,
    'unknown' / Byte,

    'm_NeighborOrientation' / NeighborOrientation,
)

CDispNeighbor = Struct(
    'm_SubNeighbors' / CDispSubNeighbor[2],
)

CDispCornerNeighbors = Struct(
    'm_Neighbors' / Int16ul[MAX_DISP_CORNER_NEIGHBORS],
    'm_nNeighbors' / Int8ul
)

ddispinfo_t = Struct(
    'startPosition' / Vector,
    'm_iDispVertStart' / Int32sl,
    'm_iDispTriStart'/Int32sl,

    'power' / Int32sl,
    'minTess'/Int32sl,
    'smoothingAngle' / Float32l,
    'contents'/Int32sl,

    'm_iMapFace' / Int16ul,

    'm_iLightmapAlphaStart' / Int32sl,
    'm_iLightmapSamplePositionStart' / Int32sl,

    'm_EdgeNeighbors' / CDispNeighbor[4],
    'm_CornerNeighbors' / CDispCornerNeighbors[4],

    'unknown' / Bytes(6),


    'm_AllowedVerts' / Int32ul[ALLOWEDVERTS_SIZE],
)

CDispVert = Struct(
    'm_vVector' / Vector,
    'm_flDist' / Float32l,
    'm_flAlpha' / Float32l,
)

CDispTri = Struct(
    'm_uiTags' / Int16ul
)


dprimitive_type = Enum(
    Int8ul,
    PRIM_TRILIST=0,
    PRIM_TRISTRIP=1,
)

dprimitive_t = Aligned(2, Struct(
    'type' / dprimitive_type,
    'firstIndex' / Int16ul,
    'indexCount' / Int16ul,
    'firstVert' / Int16ul,
    'vertCount' / Int16ul,
))

dprimvert_t = Struct(
    'pos' / Vector
)

dgamelump_t = Struct(
    'id' / PaddedString(4, "ascii"),
    'flags' / Int16ul,
    'version' / Int16ul,
    'fileofs' / Int32sl,
    'filelen' / Int32sl,
)

dgamelumpheader_t = Struct(
    'lumpCount' / Int32sl,
    'gamelump' / dgamelump_t[this.lumpCount],
)

StaticPropV6_t = Struct(
    'm_Origin' / Vector,
    'm_Angles' / QAngle,

    'm_PropType' / Int16ul,
    'm_FirstLeaf' / Int16ul,
    'm_LeafCount' / Int16ul,
    'm_Solid' / Int8ul,
    'm_Flags' / Int32ul,
    'm_Skin' / Int32sl,

    'm_FadeMinDist' / Float32l,
    'm_FadeMaxDist' / Float32l,
    'm_LightingOrigin' / Vector,


    'm_nMinDXLevel' / Int16ul,
    'm_nMaxDXLevel' / Int16ul,
    Padding(1),

    # 'm_Lighting' / Int32sl,
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

    # v5+
    'ForcedFadeScale' / Float32l,

    # v6 only
    # 'm_nMinDXLevel' / Int16ul,
    # 'm_nMaxDXLevel' / Int16ul,

    'MinCPULevel' / Int8ul,
    'MaxCPULevel' / Int8ul,
    'MinGPULevel' / Int8ul,
    'MaxGPULevel' / Int8ul,

    # v7
    'DiffuseModulation' / color32,

    # v9-10
    'DisableX360' / Int8ul,
)

StaticPropDictLump_t = Struct(
    'count' / Int32sl,
    'names' / PaddedString(STATIC_PROP_NAME_LENGTH, 'ascii')[this.count]
)
StaticPropLeafDictLump_t = Struct(
    'count' / Int32sl,
    'leafs' / Int16ul[this.count]
)
StaticPropObjectDictLump_t = Struct(
    'count' / Int32sl,
    'object' / StaticPropV10_t[this.count]
)
StaticPropLightstylesDictLump_t = Struct(
    'count' / Int32sl,
    'lightstyles' / ColorRGBExp32[this.count]
)

StaticPropLump_t = Struct(
    'dict_lump' / StaticPropDictLump_t,
    'leaf_lump' / StaticPropLeafDictLump_t,
    'object_lump' / StaticPropObjectDictLump_t,
    'lightstyles_lump' / StaticPropLightstylesDictLump_t
)

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
    'objects_lump' / DetailObjectDictLump_t,
)

DetailPropLightStyleLump_t = Struct(
    'm_Lighting' / ColorRGBExp32,
    'm_Style' / Int8ul,
)

DetailPropLightStylesLump_t = Struct(
    'count' / Int32sl,
    'styles' / DetailPropLightStyleLump_t[this.count]
)


def lump_bytes(lump_id):
    return Pointer(this.lump_header.fileofs,
                   Aligned(LUMP_ALIGNMENT, Bytes(this.lump_header.filelen)))


def lump_array(lump_id, struct):
    count = this.lump_header.filelen // struct.sizeof()
    return Pointer(this.lump_header.fileofs,
                   Aligned(LUMP_ALIGNMENT, struct[count]))


def lump_struct(lump_id, struct):
    return Pointer(this.lump_header.fileofs,
                   Aligned(LUMP_ALIGNMENT, struct))


def lump_game(lump_id, struct):
    return Pointer(this.lump_header.fileofs, struct)


header = Struct(
    # note: use rebuild for indices https://construct.readthedocs.io/en/latest/misc.html#rebuild
    'ident' / Const(b'VBSP'),
    'version' / Const(Int32sl, 20),
    'lump_t' / lump_t[HEADER_LUMPS],
    'mapRevision' / Default(Int32sl, 0)
)

lump_0 = lump_struct(LUMP_ENTITIES, CString("ascii"))
lump_1 = lump_array(LUMP_PLANES, dplane_t)
lump_2 = lump_array(LUMP_TEXDATA, dtexdata_t)
lump_3 = lump_array(LUMP_VERTEXES, Vector)
lump_4 = lump_bytes(LUMP_VISIBILITY)
lump_5 = lump_array(LUMP_NODES, dnode_t)
lump_6 = lump_array(LUMP_TEXINFO, texinfo_t)
lump_7 = lump_array(LUMP_FACES, dface_t)
lump_8 = lump_array(LUMP_LIGHTING, ColorRGBExp32)
lump_9 = lump_struct(LUMP_OCCLUSION, doccluder_t)
lump_10 = lump_array(LUMP_LEAFS, dleaf_t)
lump_11 = lump_array(LUMP_FACEIDS, dfaceid_t)
lump_12 = lump_array(LUMP_EDGES, dedge_t)
lump_13 = lump_array(LUMP_SURFEDGES, Int32sl)
lump_14 = lump_array(LUMP_MODELS, Int32sl)
lump_15 = lump_array(LUMP_WORLDLIGHTS, dworldlight_t)
lump_16 = lump_array(LUMP_LEAFFACES, Int16ul)
lump_17 = lump_array(LUMP_LEAFBRUSHES, Int16ul)
lump_18 = lump_array(LUMP_BRUSHES, dbrush_t)
lump_19 = lump_array(LUMP_BRUSHSIDES, dbrushside_t)
lump_20 = lump_array(LUMP_AREAS, darea_t)
lump_21 = lump_array(LUMP_AREAPORTALS, dareaportal_t)
lump_22 = lump_bytes(LUMP_UNUSED0)
lump_23 = lump_bytes(LUMP_UNUSED1)
lump_24 = lump_bytes(LUMP_UNUSED2)
lump_25 = lump_bytes(LUMP_UNUSED3)
lump_26 = lump_array(LUMP_DISPINFO, ddispinfo_t)
lump_27 = lump_array(LUMP_ORIGINALFACES, dface_t)
lump_28 = lump_array(LUMP_PHYSDISP, Byte)
lump_29 = lump_array(LUMP_PHYSCOLLIDE, Byte)
lump_30 = lump_array(LUMP_VERTNORMALS, Vector)
lump_31 = lump_array(LUMP_VERTNORMALINDICES, Int16ul)
lump_32 = lump_bytes(LUMP_DISP_LIGHTMAP_ALPHAS)
lump_33 = lump_array(LUMP_DISP_VERTS, CDispVert)
lump_34 = lump_array(LUMP_DISP_LIGHTMAP_SAMPLE_POSITIONS, Int8ul)
lump_35 = lump_struct(LUMP_GAME_LUMP, dgamelumpheader_t)
lump_36 = lump_array(LUMP_LEAFWATERDATA, dleafwaterdata_t)
lump_37 = lump_array(LUMP_PRIMITIVES, dprimitive_t)
lump_38 = lump_array(LUMP_PRIMVERTS, dprimvert_t)
lump_39 = lump_array(LUMP_PRIMINDICES, Int16ul)
lump_40 = lump_bytes(LUMP_PAKFILE)
lump_41 = lump_array(LUMP_CLIPPORTALVERTS, Vector)
lump_42 = lump_array(LUMP_CUBEMAPS, dcubemapsample_t)
lump_43 = Pointer(this.header.lump_t[LUMP_TEXDATA_STRING_DATA].fileofs,
                  RepeatUntil(lambda x, lst, ctx: len(lst) >=
                              ctx.header.lump_t[LUMP_TEXDATA_STRING_TABLE].filelen // Int32sl.sizeof(), CString("ascii")))
lump_44 = lump_array(LUMP_TEXDATA_STRING_TABLE, Int32sl)
lump_45 = lump_array(LUMP_OVERLAYS, doverlay_t)
lump_46 = lump_array(LUMP_LEAFMINDISTTOWATER, Int16ul)
lump_47 = lump_array(LUMP_FACE_MACRO_TEXTURE_INFO, Int16ul)
lump_48 = lump_array(LUMP_DISP_TRIS, CDispTri)
lump_49 = lump_bytes(LUMP_PHYSCOLLIDESURFACE)
lump_50 = lump_array(LUMP_WATEROVERLAYS, dwateroverlay_t)
lump_51 = lump_array(LUMP_LEAF_AMBIENT_INDEX_HDR, dleafambientindex_t)
lump_52 = lump_array(LUMP_LEAF_AMBIENT_INDEX, dleafambientindex_t)
lump_53 = lump_array(LUMP_LIGHTING_HDR, ColorRGBExp32)
lump_54 = lump_array(LUMP_WORLDLIGHTS_HDR, dworldlight_t)
lump_55 = lump_array(LUMP_LEAF_AMBIENT_LIGHTING_HDR, dleafambientlighting_t)
lump_56 = lump_array(LUMP_LEAF_AMBIENT_LIGHTING, dleafambientlighting_t)
lump_57 = lump_bytes(LUMP_XZIPPAKFILE)
lump_58 = lump_array(LUMP_FACES_HDR, dface_t)
lump_59 = lump_struct(LUMP_MAP_FLAGS, Struct(mLevelFlags=Int32ul))
lump_60 = lump_array(LUMP_OVERLAY_FADES, doverlayfade_t)
lump_61 = lump_bytes(LUMP_OVERLAY_SYSTEM_LEVELS)
lump_62 = lump_bytes(LUMP_PHYSLEVEL)
lump_63 = lump_bytes(LUMP_DISP_MULTIBLEND)

lump_prps = lump_game('prps', StaticPropLump_t)
lump_prpd = lump_game('prpd', DetailPropLump_t)
lump_tlpd = lump_game('tlpd', DetailPropLightStylesLump_t)
lump_hlpd = lump_game('hlpd', DetailPropLightStylesLump_t)

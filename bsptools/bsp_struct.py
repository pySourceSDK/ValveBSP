from __future__ import division
from __future__ import absolute_import
from __future__ import print_function
from __future__ import unicode_literals
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

dnode_t = Struct(
    'planenum' / Int32sl,
    'children' / Int32sl[2],
    'mins' / Int16sl[3],
    'maxs' / Int16sl[3],
    'firstface' / Int16ul,
    'numfaces' / Int16ul,
    'area' / Int16sl,
    'padding' / Int16sl,
)

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
    'texinfo' / Int32sl,  # lump 2
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

    'area' / Int16sl,
    'flags' / Int16sl,

    'mins' / Int16sl[3],
    'maxs' / Int16sl[3],

    'firstleafface' / Int16ul,
    'numleaffaces' / Int16ul,

    'firstleafbrush' / Int16ul,
    'numleafbrushes' / Int16ul,
    'leafWaterDataID' / Int16sl
)

dleafambientlighting_t = Struct(
    'cube' / CompressedLightCube,
    'x' / Byte,
    'y' / Byte,
    'z' / Byte,
    'pad' / Byte
)

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
    'padding' / Byte,

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
    'm_CornerNeighbors' / CDispCornerNeighbors[4],  # 9x4=36=24

    'padding' / Bytes(6),

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

dprimitive_t = Struct(
    'type' / dprimitive_type,
    'firstIndex' / Int16ul,
    'indexCount' / Int16ul,
    'firstVert' / Int16ul,
    'vertCount' / Int16ul,
    Padding(1)
)

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
    'DisableX360' / Flag,
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


def l_bytes(ctx, lump_id):
    lump_info = ctx.lump_t[lump_id]
    return Lazy(Pointer(lump_info.fileofs, Aligned(4, Bytes(lump_info.filelen))))


def l_struct(ctx, lump_id, struct=None):
    lump_info = ctx.lump_t[lump_id]
    return Lazy(Pointer(lump_info.fileofs, struct))


def l_array(ctx, lump_id, struct=None):
    lump_info = ctx.lump_t[lump_id]
    count = lump_info.filelen // struct.sizeof()
    return Lazy(Pointer(lump_info.fileofs, struct[count]))


bsp_t = Struct(
    'ident' / Const(b'VBSP'),
    'version' / Int32sl,
    'lump_t' / lump_t[HEADER_LUMPS],
    'mapRevision' / Int32sl,

    'lump_0' / l_struct(this, LUMP_ENTITIES, CString("ascii")),
    'lump_1' / l_array(this, LUMP_PLANES, dplane_t),
    'lump_2' / l_array(this, LUMP_TEXDATA, dtexdata_t),
    'lump_3' / l_array(this, LUMP_VERTEXES, Vector),
    'lump_4' / l_bytes(this, LUMP_VISIBILITY),
    'lump_5' / l_array(this, LUMP_NODES, dnode_t),
    'lump_6' / l_array(this, LUMP_TEXINFO, texinfo_t),
    'lump_7' / l_array(this, LUMP_FACES, dface_t),
    'lump_8' / l_array(this, LUMP_LIGHTING, ColorRGBExp32),
    'lump_9' / l_struct(this, LUMP_OCCLUSION, doccluder_t),
    'lump_10' / l_array(this, LUMP_LEAFS, dleaf_t),
    'lump_11' / l_array(this, LUMP_FACEIDS, dfaceid_t),
    'lump_12' / l_array(this, LUMP_EDGES, dedge_t),
    'lump_13' / l_array(this, LUMP_SURFEDGES, Int32sl),
    'lump_14' / l_array(this, LUMP_MODELS, Int32sl),
    'lump_15' / l_array(this, LUMP_WORLDLIGHTS, dworldlight_t),
    'lump_16' / l_array(this, LUMP_LEAFFACES, Int16ul),
    'lump_17' / l_array(this, LUMP_LEAFBRUSHES, Int16ul),
    'lump_18' / l_array(this, LUMP_BRUSHES, dbrush_t),
    'lump_19' / l_array(this, LUMP_BRUSHSIDES, dbrushside_t),
    'lump_20' / l_array(this, LUMP_AREAS, darea_t),
    'lump_21' / l_array(this, LUMP_AREAPORTALS, dareaportal_t),
    'lump_22' / l_bytes(this, LUMP_UNUSED0),
    'lump_23' / l_bytes(this, LUMP_UNUSED1),
    'lump_24' / l_bytes(this, LUMP_UNUSED2),
    'lump_25' / l_bytes(this, LUMP_UNUSED3),
    'lump_26' / l_array(this, LUMP_DISPINFO, ddispinfo_t),
    'lump_27' / l_array(this, LUMP_ORIGINALFACES, dface_t),
    'lump_28' / l_array(this, LUMP_PHYSDISP, Byte),
    'lump_29' / l_array(this, LUMP_PHYSCOLLIDE, Byte),
    'lump_30' / l_array(this, LUMP_VERTNORMALS, Vector),
    'lump_31' / l_array(this, LUMP_VERTNORMALINDICES, Int16ul),
    'lump_32' / l_bytes(this, LUMP_DISP_LIGHTMAP_ALPHAS),
    'lump_33' / l_array(this, LUMP_DISP_VERTS, CDispVert),
    'lump_34' / l_array(this, LUMP_DISP_LIGHTMAP_SAMPLE_POSITIONS, Int8ul),
    #'lump_35' / l_struct(this, LUMP_GAME_LUMP, dgamelumpheader_t),
    'lump_35' / l_bytes(this, LUMP_GAME_LUMP),
    'lump_36' / l_array(this, LUMP_LEAFWATERDATA, dleafwaterdata_t),
    'lump_37' / l_array(this, LUMP_PRIMITIVES, dprimitive_t),
    'lump_38' / l_array(this, LUMP_PRIMVERTS, dprimvert_t),
    'lump_39' / l_array(this, LUMP_PRIMINDICES, Int16ul),
    'lump_40' / l_bytes(this, LUMP_PAKFILE),
    'lump_41' / l_array(this, LUMP_CLIPPORTALVERTS, Vector),
    'lump_42' / l_array(this, LUMP_CUBEMAPS, dcubemapsample_t),
    'lump_43' / Lazy(Pointer(this.lump_t[LUMP_TEXDATA_STRING_DATA].fileofs,
                             RepeatUntil(lambda x, lst, ctx: len(lst) >=
                                         ctx.lump_t[LUMP_TEXDATA_STRING_TABLE].filelen // Int32sl.sizeof(), CString("ascii")))),
    'lump_44' / l_array(this, LUMP_TEXDATA_STRING_TABLE, Int32sl),
    'lump_45' / l_array(this, LUMP_OVERLAYS, doverlay_t),
    'lump_46' / l_array(this, LUMP_LEAFMINDISTTOWATER, Int16ul),
    'lump_47' / l_array(this, LUMP_FACE_MACRO_TEXTURE_INFO, Int16ul),
    'lump_48' / l_array(this, LUMP_DISP_TRIS, CDispTri),
    'lump_49' / l_bytes(this, LUMP_PHYSCOLLIDESURFACE),
    'lump_50' / l_array(this, LUMP_WATEROVERLAYS, dwateroverlay_t),
    'lump_51' / l_array(this, LUMP_LEAF_AMBIENT_INDEX_HDR, dleafambientindex_t),
    'lump_52' / l_array(this, LUMP_LEAF_AMBIENT_INDEX, dleafambientindex_t),
    'lump_53' / l_array(this, LUMP_LIGHTING_HDR, ColorRGBExp32),
    'lump_54' / l_array(this, LUMP_WORLDLIGHTS_HDR, dworldlight_t),
    'lump_55' / l_array(this, LUMP_LEAF_AMBIENT_LIGHTING_HDR,
                        dleafambientlighting_t),
    'lump_56' / l_array(this, LUMP_LEAF_AMBIENT_LIGHTING,
                        dleafambientlighting_t),
    'lump_57' / l_bytes(this, LUMP_XZIPPAKFILE),
    'lump_58' / l_array(this, LUMP_FACES_HDR, dface_t),
    'lump_59' / l_struct(this, LUMP_MAP_FLAGS, Struct('mLevelFlags' / Int32ul)),
    'lump_60' / l_array(this, LUMP_OVERLAY_FADES, doverlayfade_t),
    'lump_61' / l_bytes(this, LUMP_OVERLAY_SYSTEM_LEVELS),
    'lump_62' / l_bytes(this, LUMP_PHYSLEVEL),
    'lump_63' / l_bytes(this, LUMP_DISP_MULTIBLEND)
)

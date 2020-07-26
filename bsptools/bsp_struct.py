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
dcubemapsample_t = Struct(
    'origin' / Int32sl[3],
    'size' / Int32sl
)


bsp_t = Struct(
    'ident' / Const(b'VBSP'),
    'version' / Int32sl,
    'lump_t' / lump_t[HEADER_LUMPS],
    'mapRevision' / Int32sl,

    # 0 Entities
    'lump_0' / Lazy(Pointer(this.lump_t[0].fileofs, CString("ascii"))),

    # 1 Planes
    'lump_1' / Lazy(Pointer(this.lump_t[1].fileofs,
                            dplane_t[this.lump_t[1].filelen // dplane_t.sizeof()])),
    # 2 Texture Data
    'lump_2' / Lazy(Pointer(this.lump_t[2].fileofs,
                            dtexdata_t[this.lump_t[2].filelen // dtexdata_t.sizeof()])),
    # 3 Vertexes
    'lump_3' / Lazy(Pointer(this.lump_t[3].fileofs,
                            Vector[this.lump_t[3].filelen // Vector.sizeof()])),
    # 4 Visibility
    # 'lump_4' / TODO

    # 5 Nodes
    'lump_5' / Lazy(Pointer(this.lump_t[5].fileofs,
                            dnode_t[this.lump_t[5].filelen // dnode_t.sizeof()])),
    # 6 Texture Info
    'lump_6' / Lazy(Pointer(this.lump_t[6].fileofs,
                            texinfo_t[this.lump_t[6].filelen // texinfo_t.sizeof()])),
    # 7 Faces
    'lump_7' / Lazy(Pointer(this.lump_t[7].fileofs,
                            dface_t[this.lump_t[7].filelen // dface_t.sizeof()])),
    # 8 Lightmaps
    'lump_8' / Lazy(Pointer(this.lump_t[8].fileofs,
                            ColorRGBExp32[this.lump_t[8].filelen // ColorRGBExp32.sizeof()])),
    # 9 Occlusion / TODO (not ready)
    # 'lump_9' / Lazy(Pointer(this.lump_t[9].fileofs,
    #                   [this.lump_t[9].filelen // ColorRGBExp32.sizeof()])),

    # 10 leafs
    # 'lump_10' / TODO

    # 11 FaceIds
    'lump_11' / Lazy(Pointer(this.lump_t[11].fileofs,
                             dfaceid_t[this.lump_t[11].filelen // dfaceid_t.sizeof()])),
    # 12 Edges
    'lump_12' / Lazy(Pointer(this.lump_t[12].fileofs,
                             dedge_t[this.lump_t[12].filelen // dedge_t.sizeof()])),
    # 13 Surfedges
    'lump_13' / Lazy(Pointer(this.lump_t[13].fileofs,
                             Int32sl[this.lump_t[13].filelen // Int32sl.sizeof()])),
    # 14 Models
    'lump_14' / Lazy(Pointer(this.lump_t[14].fileofs,
                             Int32sl[this.lump_t[14].filelen // Int32sl.sizeof()])),
    # 15 Worldlights
    'lump_15' / Lazy(Pointer(this.lump_t[15].fileofs,
                             dworldlight_t[this.lump_t[15].filelen // dworldlight_t.sizeof()])),
    # 16 Leaf Faces
    'lump_16' / Lazy(Pointer(this.lump_t[16].fileofs,
                             Int16ul[this.lump_t[16].filelen // Int16ul.sizeof()])),
    # 17 Leaf Brushes
    'lump_17' / Lazy(Pointer(this.lump_t[17].fileofs,
                             Int16ul[this.lump_t[17].filelen // Int16ul.sizeof()])),
    # 18 Brushes
    'lump_18' / Lazy(Pointer(this.lump_t[18].fileofs,
                             dbrush_t[this.lump_t[18].filelen // dbrush_t.sizeof()])),
    # 19 Brush Sides
    'lump_19' / Lazy(Pointer(this.lump_t[19].fileofs,
                             dbrushside_t[this.lump_t[19].filelen // dbrushside_t.sizeof()])),
    # 20 Areas
    'lump_20' / Lazy(Pointer(this.lump_t[20].fileofs,
                             darea_t[this.lump_t[20].filelen // darea_t.sizeof()])),
    # 21 Areaportals
    'lump_21' / Lazy(Pointer(this.lump_t[21].fileofs,
                             dareaportal_t[this.lump_t[21].filelen // dareaportal_t.sizeof()])),
    # 22 unused
    # 23 unused
    # 24 unused
    # 25 unused
    # 26 Disp Info
    # 27 Original Faces
    # 28 Phys Disp
    # 29 Phys Collide
    # 30 Vert Normals
    # 31 Vert Normal Indices
    # 32 unused
    # 33 Disp Verts
    # 34 Disp Lightmap Sample Pos
    # 35 Game Lump
    # 36 Leaf Water Data
    # 37 Primitives
    # 38 Prim Verts
    # 39 Prim Indices
    # 40 PakFile
    # 41 Clip Portal Verts

    # 42 Cubemaps
    'lump_42' / Lazy(Pointer(this.lump_t[42].fileofs,
                             dcubemapsample_t[this.lump_t[42].filelen // dcubemapsample_t.sizeof()])),
    # 43 Texture String Data
    'lump_43' / Lazy(Pointer(this.lump_t[43].fileofs,
                             RepeatUntil(lambda x, lst, ctx: len(lst) >=
                                         ctx.lump_t[44].filelen // Int32sl.sizeof(), CString("ascii")))),
    # 44 Texture String Table
    'lump_44' / Lazy(Pointer(this.lump_t[44].fileofs,
                             Int32sl[this.lump_t[44].filelen // Int32sl.sizeof()])),


    # 45 Overlays
    # 46 Leaf Min Dist to Water
    # 47 Face Macro Texture Info
    # 48 Disp Triangles
    # 49 Phys Collide Surface
    # 50 Water Overlays

    # 51 Leaf Ambient Index HDR
    'lump_51' / Lazy(Pointer(this.lump_t[51].fileofs,
                             dleafambientindex_t[this.lump_t[52].filelen // dleafambientindex_t.sizeof()])),
    # 52 Leaf Ambient Index
    'lump_52' / Lazy(Pointer(this.lump_t[52].fileofs,
                             dleafambientindex_t[this.lump_t[53].filelen // dleafambientindex_t.sizeof()])),
    # 53 Lightmaps HDR
    'lump_53' / Lazy(Pointer(this.lump_t[53].fileofs,
                             ColorRGBExp32[this.lump_t[53].filelen // ColorRGBExp32.sizeof()])),
    # 54 Worldlights HDR
    'lump_54' / Lazy(Pointer(this.lump_t[54].fileofs,
                             dworldlight_t[this.lump_t[54].filelen // dworldlight_t.sizeof()])),
    # 55 Leaf Ambient Samples HDR
    'lump_55' / Lazy(Pointer(this.lump_t[55].fileofs,
                             dleafambientlighting_t[this.lump_t[55].filelen // dleafambientlighting_t.sizeof()])),
    # 56 Leaf Ambient Samples
    'lump_56' / Lazy(Pointer(this.lump_t[56].fileofs,
                             dleafambientlighting_t[this.lump_t[56].filelen // dleafambientlighting_t.sizeof()])),

    # 57 XZIP PakFile
    # 58 Faces HDR
    'lump_58' / Lazy(Pointer(this.lump_t[58].fileofs,
                             dface_t[this.lump_t[58].filelen // dface_t.sizeof()])),
    # 59 Map Flags
    # 60 Overlay Fades
    # 61 Overlay System Levels
    # 62 Phys Level
    # 63 Disp Multiblend

)

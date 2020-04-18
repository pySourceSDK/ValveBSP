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

bsp_t = Struct(
    'ident' / Const(b'VBSP'),
    'version' / Int32sl,
    'lump_t' / lump_t[HEADER_LUMPS],
    'mapRevision' / Int32sl,

    # 'lump_0' / TODO

    'lump_1' / Pointer(this.lump_t[1].fileofs,
                       dplane_t[this.lump_t[1].filelen // dplane_t.sizeof()]),
    'lump_2' / Pointer(this.lump_t[2].fileofs,
                       dtexdata_t[this.lump_t[2].filelen // dtexdata_t.sizeof()]),
    'lump_3' / Pointer(this.lump_t[3].fileofs,
                       Vector[this.lump_t[3].filelen // Vector.sizeof()]),
    # 'lump_4' / TODO

    'lump_5' / Pointer(this.lump_t[5].fileofs,
                       dnode_t[this.lump_t[5].filelen // dnode_t.sizeof()]),
    'lump_6' / Pointer(this.lump_t[6].fileofs,
                       texinfo_t[this.lump_t[6].filelen // texinfo_t.sizeof()]),
    'lump_7' / Pointer(this.lump_t[7].fileofs,
                       dface_t[this.lump_t[7].filelen // dface_t.sizeof()]),
    'lump_8' / Pointer(this.lump_t[8].fileofs,
                       ColorRGBExp32[this.lump_t[8].filelen // ColorRGBExp32.sizeof()]),
    # 'lump_9' / Pointer(this.lump_t[9].fileofs,
    #                   [this.lump_t[9].filelen // ColorRGBExp32.sizeof()]),

    'lump_11' / Pointer(this.lump_t[11].fileofs,
                        dfaceid_t[this.lump_t[11].filelen // dfaceid_t.sizeof()]),
)

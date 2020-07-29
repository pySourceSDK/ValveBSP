

from __future__ import unicode_literals
from __future__ import print_function
from __future__ import division
from __future__ import absolute_import
from builtins import object
from builtins import range
from builtins import str
from builtins import open
from future import standard_library
standard_library.install_aliases()

from construct import *  # NOQA: #402
from collections.abc import MutableMapping  # NOQA: #402
from bsptools.bsp_struct import *  # NOQA: #402


LUMPS_UNSUPORTED = [4, 49, 61, 62, 63]
LUMPS_UNUSED = [22, 23, 24, 25, 32]

GAMELUMP_IDS = {
    'prps': StaticPropLump_t,
    'prpd': DetailPropLump_t,
    'tlpd': DetailPropLightStylesLump_t,
    'hlpd': DetailPropLightStylesLump_t,
}

LUMP_ENTITIES = 0  # NOQA: #221
LUMP_PLANES = 1
LUMP_TEXDATA = 2
LUMP_VERTEXES = 3
LUMP_VISIBILITY = 4
LUMP_NODES = 5
LUMP_TEXINFO = 6
LUMP_FACES = 7
LUMP_LIGHTING = 8
LUMP_OCCLUSION = 9
LUMP_LEAFS = 10
LUMP_FACEIDS = 11
LUMP_EDGES = 12
LUMP_SURFEDGES = 13
LUMP_MODELS = 14
LUMP_WORLDLIGHTS = 15
LUMP_LEAFFACES = 16
LUMP_LEAFBRUSHES = 17
LUMP_BRUSHES = 18
LUMP_BRUSHSIDES = 19
LUMP_AREAS = 20
LUMP_AREAPORTALS = 21
LUMP_UNUSED0 = 22
LUMP_UNUSED1 = 23
LUMP_UNUSED2 = 24
LUMP_UNUSED3 = 25
LUMP_DISPINFO = 26
LUMP_ORIGINALFACES = 27
LUMP_PHYSDISP = 28
LUMP_PHYSCOLLIDE = 29
LUMP_VERTNORMALS = 30
LUMP_VERTNORMALINDICES = 31
LUMP_DISP_LIGHTMAP_ALPHAS = 32
LUMP_DISP_VERTS = 33
LUMP_DISP_LIGHTMAP_SAMPLE_POSITIONS = 34
LUMP_GAME_LUMP = 35
LUMP_LEAFWATERDATA = 36
LUMP_PRIMITIVES = 37
LUMP_PRIMVERTS = 38
LUMP_PRIMINDICES = 39
LUMP_PAKFILE = 40
LUMP_CLIPPORTALVERTS = 41
LUMP_CUBEMAPS = 42
LUMP_TEXDATA_STRING_DATA = 43
LUMP_TEXDATA_STRING_TABLE = 44
LUMP_OVERLAYS = 45
LUMP_LEAFMINDISTTOWATER = 46
LUMP_FACE_MACRO_TEXTURE_INFO = 47
LUMP_DISP_TRIS = 48
LUMP_PHYSCOLLIDESURFACE = 49
LUMP_WATEROVERLAYS = 50
LUMP_LEAF_AMBIENT_INDEX_HDR = 51
LUMP_LEAF_AMBIENT_INDEX = 52
LUMP_LIGHTING_HDR = 53
LUMP_WORLDLIGHTS_HDR = 54
LUMP_LEAF_AMBIENT_LIGHTING_HDR = 55
LUMP_LEAF_AMBIENT_LIGHTING = 56
LUMP_XZIPPAKFILE = 57
LUMP_FACES_HDR = 58
LUMP_MAP_FLAGS = 59
LUMP_OVERLAY_FADES = 60
LUMP_OVERLAY_SYSTEM_LEVELS = 61
LUMP_PHYSLEVEL = 62
LUMP_DISP_MULTIBLEND = 63


class Bsp(MutableMapping):
    """Contains all the data from a Bsp file"""

    def __init__(self, path=None):
        """Creates an empty instance of Bsp."""

        self.ident = None
        self.version = None
        self.offsets = None
        self.mapRevision = None
        self.lumps = [None] * 64
        self.gamelumps = {}
        self.construct = None

        if path:
            self.f = open(path, "rb")

            self.construct = bsp_t.parse_stream(self.f)

            self.ident = self.construct['ident']
            self.version = self.construct['version']
            self.lump_t = self.construct['lump_t']
            self.mapRevision = self.construct['mapRevision']

    def __setitem__(self, key, value):
        return

    def __getitem__(self, index):

        if isinstance(index, str):  # It's a gamelump id

            if index not in self.gamelumps:
                gamelump = False
                for lump in self[LUMP_GAME_LUMP].gamelump:
                    if lump.id == index and index in GAMELUMP_IDS:
                        gamelump = Pointer(lump.fileofs, GAMELUMP_IDS[index])
                        continue
                if not gamelump:
                    raise IndexError('Lump ID not Found')

                self.gamelumps[index] = gamelump.parse_stream(self.f)

            return self.gamelumps[index]

        elif isinstance(index, int):  # It's a lump id

            if index not in range(64):
                raise IndexError("Lump ID out of range")
            if index in LUMPS_UNSUPORTED:
                raise IndexError("Lump ID not Supported")
            if index in LUMPS_UNUSED:
                raise IndexError("Lump ID is unused")
            if not self.lumps[index]:
                if self.construct:
                    self.lumps[index] = self.construct['lump_'+str(index)]()
                else:
                    return None

            if index == 40:
                return bytearray(self.lumps[index])

            return self.lumps[index]

    def __delitem__(self, key):
        del self.store[self.__keytransform__(key)]

    def __iter__(self):
        return self.item(self.lumps)

    def __len__(self, index):
        return 64

    def __keytransform__(self, key):
        print('key')
        print(key)
        return key

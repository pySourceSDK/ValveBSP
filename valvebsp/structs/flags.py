from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals
from future import standard_library
standard_library.install_aliases()

from construct import *  # NOQA: #402

contents_flags32 = FlagsEnum(Int32ul,
                             CONTENTS_SOLID=1,
                             CONTENTS_WINDOW=2,
                             CONTENTS_AUX=4,
                             CONTENTS_GRATE=8,
                             CONTENTS_SLIME=16,
                             CONTENTS_WATER=32,
                             CONTENTS_BLOCKLOS=64,
                             CONTENTS_OPAQUE=128,
                             CONTENTS_TESTFOGVOLUME=256,
                             CONTENTS_UNUSED=512,
                             CONTENTS_UNUSED6=1024,
                             CONTENTS_TEAM1=2048,
                             CONTENTS_TEAM2=4096,
                             CONTENTS_IGNORE_NODRAW_OPAQUE=8192,
                             CONTENTS_MOVEABLE=16384,
                             CONTENTS_AREAPORTAL=32768,
                             CONTENTS_PLAYERCLIP=65536,
                             CONTENTS_MONSTERCLIP=131072,
                             CONTENTS_CURRENT_0=262144,
                             CONTENTS_CURRENT_90=524288,
                             CONTENTS_CURRENT_180=1048576,
                             CONTENTS_CURRENT_270=2097152,
                             CONTENTS_CURRENT_UP=4194304,
                             CONTENTS_CURRENT_DOWN=8388608,
                             CONTENTS_ORIGIN=16777216,
                             CONTENTS_MONSTER=33554432,
                             CONTENTS_DEBRIS=67108864,
                             CONTENTS_DETAIL=134217728,
                             CONTENTS_TRANSLUCENT=268435456,
                             CONTENTS_LADDER=536870912,
                             CONTENTS_HITBOX=1073741824)
dispinfo_flags8 = FlagsEnum(Int8ul,
                            COLL_UNUSED=1,
                            COLL_NOPHYS=2,
                            COLL_NOHULL=4,
                            COLL_NORAY=8)
texinfo_flags32 = FlagsEnum(Int32ul,
                            SURF_LIGHT=1,
                            SURF_SKY2D=2,
                            SURF_SKY=4,
                            SURF_WARP=8,
                            SURF_TRANS=16,
                            SURF_NOPORTAL=32,
                            SURF_TRIGGER=64,
                            SURF_NODRAW=128,
                            SURF_HINT=256,
                            SURF_SKIP=512,
                            SURF_NOLIGHT=1024,
                            SURF_BUMPLIGHT=2048,
                            SURF_NOSHADOWS=4096,
                            SURF_NODECALS=8192,
                            SURF_NOCHOP=16384,
                            SURF_HITBOX=32768)

dworldlight_flags32 = FlagsEnum(Int32sl,
                                DWL_FLAGS_INAMBIENTCUBE=0,
                                DWL_FLAGS_CASTENTITYSHADOWS=1)

dgamelump_flags16 = FlagsEnum(Int16ul,
                              GAMELUMPFLAG_COMPRESSED=1)

doccluderdata_flags32 = FlagsEnum(Int32sl,
                                  OCCLUDER_FLAGS_INACTIVE=1)

levelflags_flags32 = FlagsEnum(Int32ul,
                               BAKED_STATIC_PROP_LIGHTING_NONHDR=1,
                               BAKED_STATIC_PROP_LIGHTING_HDR=2)

dleaf_flags7 = FlagsEnum(BitsInteger(7),
                         LEAF_FLAGS_SKY=1,
                         LEAF_FLAGS_RADIAL=2,
                         LEAF_FLAGS_SKY2D=4,
                         LEAF_FLAGS_CONTAINS_DETAILOBJECTS=8)

prps_flags8 = FlagsEnum(Int8ul,
                        STATIC_PROP_FLAG_FADES=1,
                        STATIC_PROP_USE_LIGHTING_ORIGIN=2,
                        STATIC_PROP_NO_DRAW=4,
                        STATIC_PROP_IGNORE_NORMALS=8,
                        STATIC_PROP_NO_SHADOW=16,
                        STATIC_PROP_SCREEN_SPACE_FADE_OBSOLETE=32,
                        STATIC_PROP_NO_PER_VERTEX_LIGHTING=64,
                        STATIC_PROP_NO_SELF_SHADOWING=128)

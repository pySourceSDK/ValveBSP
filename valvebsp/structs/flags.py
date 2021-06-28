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

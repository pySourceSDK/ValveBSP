"""
Common Structures
=================

These are reoccuring data structures that you'll see reused throughout Bsp.
"""

from __future__ import division
from __future__ import absolute_import
from __future__ import print_function
from __future__ import unicode_literals
from future import standard_library
standard_library.install_aliases()

from construct import *  # NOQA: E402
from valvebsp.constants import *  # NOQA: E402

Vector = Struct('x' / Float32l, 'y' / Float32l, 'z' / Float32l)


Vector2D = Struct('x' / Float32l, 'y' / Float32l)
Vector4D = Struct('x' / Float32l, 'y' / Float32l,
                  'z' / Float32l, 'w' / Float32l)
RadianEuler = Struct('x' / Float32l, 'y' / Float32l, 'z' / Float32l)
QAngle = Struct('x' / Float32l, 'y' / Float32l, 'z' / Float32l)
Quaternion = Struct('x' / Float32l, 'y' / Float32l,
                    'z' / Float32l, 'w' / Float32l)
color32 = Struct('r' / Int8ul, 'g' / Int8ul, 'b' / Int8ul, 'a' / Int8ul)
ColorRGBExp32 = Struct('r' / Byte, 'g' / Byte, 'b' /
                       Byte, 'exponent' / Byte)
CompressedLightCube = Struct('color' / ColorRGBExp32[6])


def lump_bytes(lump_id, header):
    return Pointer(header.fileofs, Aligned(4, Bytes(header.filelen).compile()))


def lump_array(lump_id, struct, header):
    count = header.filelen // struct.sizeof()
    return Pointer(header.fileofs, Aligned(4, struct[count])).compile()


def lump_struct(lump_id, struct, header):
    return Pointer(header.fileofs, Aligned(4, struct.compile()))


def lump_game(lump_id, struct, header):
    return Pointer(header.fileofs, struct)


def lump_dud(lump_id, header):
    return Pointer(header.fileofs, Bytes(0))

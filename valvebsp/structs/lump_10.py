"""
.. Lump 10 - Leafs

This lump contains an array of :any:`dleaf_tV1` or :any:`dleaf_tV1` (Version detection is automatic).
"""

from __future__ import division
from __future__ import absolute_import
from __future__ import print_function
from __future__ import unicode_literals
from future import standard_library
standard_library.install_aliases()

from construct import *  # NOQA: #402
from valvebsp.structs.common import *  # NOQA: #402
from valvebsp.structs.flags import contents_flags32, dleaf_flags7  # NOQA: #402

# The Source ``dleaf_t`` packs two C bitfields into a single little-endian
# 16-bit short: ``area`` is the low 9 bits, ``flags`` the high 7 bits.
# ``construct.Bitwise`` slices bytes MSB-first/big-endian, which does not match
# that little-endian packing, so the pair must be byte-swapped before the bit
# fields are read (``flags`` first, then ``area``, to line up with the swap).
# ``area`` and ``flags`` are also exposed as flat read aliases for convenience;
# to edit them and have the change persist, set ``leaf.areaflags.area`` /
# ``leaf.areaflags.flags`` (the packed field is the source of truth on build).
dleaf_areaflags = ByteSwapped(Bitwise(Struct(
    'flags' / dleaf_flags7,
    'area' / BitsInteger(9),
)))

dleaf_tV0 = Aligned(4, Struct(
    'contents' / contents_flags32,
    'cluster' / Int16sl,

    'areaflags' / dleaf_areaflags,
    'area' / Computed(this.areaflags.area),
    'flags' / Computed(this.areaflags.flags),

    'mins' / Int16sl[3],
    'maxs' / Int16sl[3],

    'firstLeafFace' / Int16ul * "index into :ref:`lump 16<lump_16>`",
    'numLeafFaces' / Int16ul,

    'firstLeafBrush' / Int16ul *
    "index into :ref:`lump 17<lump_17>`",
    'numLeafBrushes' / Int16ul,
    'leafWaterDataID' / Int16sl *
    "index into :ref:`lump 36<lump_36>`",

    'ambientLighting' / CompressedLightCube
))

dleaf_tV1 = Aligned(4, Struct(
    'contents' / contents_flags32,
    'cluster' / Int16sl,

    'areaflags' / dleaf_areaflags,
    'area' / Computed(this.areaflags.area),
    'flags' / Computed(this.areaflags.flags),

    'mins' / Int16sl[3],
    'maxs' / Int16sl[3],


    'firstLeafFace' / Int16ul * "index into :ref:`lump 16<lump_16>`",
    'numLeafFaces' / Int16ul,

    'firstLeafBrush' / Int16ul *
    "index into :ref:`lump 17<lump_17>`",
    'numLeafBrushes' / Int16ul,
    'leafWaterDataID' / Int16sl *
    "index into :ref:`lump 36<lump_36>`"
))


@lump_array
@lump_version([0, 1])
def lump_10(header, profile=None):
    if header.version == 0:
        return dleaf_tV0
    elif header.version == 1:
        return dleaf_tV1

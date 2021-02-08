"""
Lump 15 - Worldlights
=====================

This lump contains an array of :any:`dworldlight_tV0` or :any:`dworldlight_tV1` (Version detection is automatic).
"""

from __future__ import division
from __future__ import absolute_import
from __future__ import print_function
from __future__ import unicode_literals
from future import standard_library
standard_library.install_aliases()

from construct import *  # NOQA: #402
from valvebsp.constants import *  # NOQA: #402
from valvebsp.exceptions import *  # NOQA: #402
from valvebsp.structs.common import *  # NOQA: #402

emittype_t = Enum(
    Int32ul,
    emit_surface=0,
    emit_point=1,
    emit_spotlight=2,
    emit_skylight=3,
    emit_quakelight=4,
    emit_skyambient=5
)

dworldlight_tV0 = Struct(
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
    'constantAttn' / Float32l,
    'linearAttn' / Float32l,
    'quadraticAttn' / Float32l,
    'flags' / Int32sl,
    'texinfo' / Int32sl * "refers to lump 2",
    'owner' / Int32sl,  # lump 0
)

dworldlight_tV1 = Struct(
    'origin' / Vector,
    'intensity' / Vector,
    'normal' / Vector,
    'shadow_cast_offset' / Vector,
    'cluster' / Int32sl,
    'type' / emittype_t,
    'style' / Int32sl,
    'stopdot' / Float32l,
    'stopdot2' / Float32l,
    'exponent' / Float32l,
    'radius' / Float32l,
    'constantAttn' / Float32l,
    'linearAttn' / Float32l,
    'quadraticAttn' / Float32l,
    'flags' / Int32sl,
    'texinfo' / Int32sl * "refers to lump 2",
    'owner' / Int32sl,  # lump 0
)


def lump_15(header, profile=None):
    if header.version == 0:
        return lump_array(LUMP_WORLDLIGHTS, dworldlight_tV0, header)
    elif header.version == 1:
        return lump_array(LUMP_WORLDLIGHTS, dworldlight_tV1, header)
    else:
        raise LumpVersionUnsupportedError(header.version)

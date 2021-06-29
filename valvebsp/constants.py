from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals
from future import standard_library
standard_library.install_aliases()

from valvebsp.lumps import *
from valvebsp.profiles import *


HEADER_LUMPS = 64  #:
OVERLAY_BSP_FACE_COUNT = 64  #:
WATEROVERLAY_BSP_FACE_COUNT = 256  #:
MAX_MAP_LEAFS = 65536  #:

MAX_MAP_DISP_POWER = 4  #:


def NUM_DISP_POWER_VERTS(power):
    return (1 * (2 ** power) + 1) * (1 * (2 ** power) + 1)


MAX_DISPVERTS = NUM_DISP_POWER_VERTS(4)  #:


def PAD_NUMBER(number, boundary):
    return (number + boundary - 1) // boundary * boundary


ALLOWEDVERTS_SIZE = PAD_NUMBER(MAX_DISPVERTS, 32) // 32  #:
MAX_DISP_CORNER_NEIGHBORS = 4  #:

STATIC_PROP_NAME_LENGTH = 128  #:
DETAIL_NAME_LENGTH = 128  #:

LUMP_ALIGNMENT = 4  #:

from __future__ import division
from __future__ import absolute_import
from __future__ import print_function
from __future__ import unicode_literals
from future import standard_library
standard_library.install_aliases()

from construct import *  # NOQA: #402
from bsptools.constants import *  # NOQA: #402
from bsptools.exceptions import *  # NOQA: #402
from bsptools.structs.common_struct import *  # NOQA: #402

dareaportal_t = Struct(
    'm_PortalKey' / Int16ul,
    'otherarea' / Int16ul,
    'm_FirstClipPortalVert' / Int16ul,
    'm_nClipPortalVerts' / Int16ul,
    'planenum' / Int32sl
)


def lump_21(header, profile=None):
    if header.version != 0:
        raise LumpVersionUnsupportedError(header.version)
    return lump_array(LUMP_AREAPORTALS, dareaportal_t, header)

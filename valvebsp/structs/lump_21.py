"""
Lump 21 - Area Portals
======================

This lump contains an array of :any:`dareaportal_t`.
"""

from __future__ import division
from __future__ import absolute_import
from __future__ import print_function
from __future__ import unicode_literals
from future import standard_library
standard_library.install_aliases()

from construct import *  # NOQA: #402
from valvebsp.structs.common import *  # NOQA: #402

dareaportal_t = Struct(
    'portalKey' / Int16ul,
    'otherArea' / Int16ul,
    'firstClipPortalVert' / Int16ul,
    'clipPortalVerts' / Int16ul,
    'planeNum' / Int32sl
)


@lump_array
@lump_version(0)
def lump_21(header, profile=None):
    return dareaportal_t

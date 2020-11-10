"""
Lump 52 - Lightmap Page Infos ...or Leaf Ambient Index
======================================================

This lump contains an array of :any:`dleafambientindex_t` (:ref:`as seen in lump_51<lump_51>`).
"""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals
from future import standard_library
standard_library.install_aliases()

from bsptools.constants import *  # NOQA: #402
from bsptools.exceptions import *  # NOQA: #402
from bsptools.structs.common import *  # NOQA #402
from bsptools.structs.lump_51 import dleafambientindex_t  # NOQA #402


def lump_52(header, profile=None):
    if header.version == 0:
        return lump_array(LUMP_LEAF_AMBIENT_INDEX, dleafambientindex_t, header)
    elif header.version == 1:
        return lump_array(LUMP_LEAF_AMBIENT_INDEX, dleafambientindex_t, header)
    else:
        raise LumpVersionUnsupportedError(header.version)

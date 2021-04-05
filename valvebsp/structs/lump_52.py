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

from valvebsp.structs.common import *  # NOQA #402
from valvebsp.structs.lump_51 import dleafambientindex_t  # NOQA #402


@lump_array
@lump_version([0, 1])
def lump_52(header, profile=None):
    return dleafambientindex_t

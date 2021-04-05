"""
Lump 55 - Leaf Ambient Lighting HDR
===================================

This lump contains an array of :any:`dleafambientlighting_t`.
It is the HDR version of :ref:`lump 56<lump_56>`.
"""

from __future__ import division
from __future__ import absolute_import
from __future__ import print_function
from __future__ import unicode_literals
from future import standard_library
standard_library.install_aliases()

from valvebsp.structs.common import *  # NOQA: #402
from valvebsp.structs.lump_56 import dleafambientlighting_t  # NOQA: #402


@lump_array
def lump_55(header, profile=None):
    if header.version == 1:
        return dleafambientlighting_t

    elif header.version == header.filelen:
        # This is obviously a mistake in the bsp header, let's assume v1
        # (seen in css map once)
        return dleafambientlighting_t

    else:
        raise LumpVersionUnsupportedError(header.version)

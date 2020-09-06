from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals
from future import standard_library
standard_library.install_aliases()

from bsptools.constants import *  # NOQA: #402
from bsptools.exceptions import *  # NOQA: #402
from bsptools.structs.common_struct import *  # NOQA #402
from bsptools.structs.lump_55 import dleafambientlighting_t  # NOQA: #402


def lump_56(header, profile=None):
    if header.version == 1:
        return lump_array(LUMP_LEAF_AMBIENT_LIGHTING,
                          dleafambientlighting_t, header)

    elif header.version == header.filelen:
        # This is obviously a mistake in the bsp header, let's assume v1
        # (seen in css map once)
        return lump_array(LUMP_LEAF_AMBIENT_LIGHTING,
                          dleafambientlighting_t, header)

    else:
        raise LumpVersionUnsupportedError(header.version)

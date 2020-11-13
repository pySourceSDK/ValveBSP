"""
Lump hlpd - Prop Detail Lighting HDR
====================================

This lump is the HDR version of :ref:`lump tlpd<lump_tlpd>`, its structure is identical
"""

from __future__ import division
from __future__ import absolute_import
from __future__ import print_function
from __future__ import unicode_literals
from future import standard_library
standard_library.install_aliases()

from construct import *  # NOQA: #402
from bsptools.constants import *  # NOQA: #402
from bsptools.exceptions import *  # NOQA: #402
from bsptools.structs.common import *  # NOQA #402
from bsptools.structs.lump_tlpd import DetailPropLightStylesLump_t  # NOQA #402


def lump_hlpd(header, profile=None):
    if header.version != 0:
        raise LumpVersionUnsupportedError(header.version)

    return lump_game('hlpd', DetailPropLightStylesLump_t, header)

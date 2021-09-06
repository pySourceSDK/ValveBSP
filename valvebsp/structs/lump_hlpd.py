"""
Lump hlpd - Prop Detail Lighting HDR
====================================

This lump is the HDR version of :ref:`lump tlpd<lump_tlpd>`, its structure is identical.
"""

from __future__ import division
from __future__ import absolute_import
from __future__ import print_function
from __future__ import unicode_literals
from future import standard_library
standard_library.install_aliases()

from valvebsp.structs.common import *  # NOQA #402
from valvebsp.structs.lump_tlpd import DetailPropLightStyle_t  # NOQA #402


@lump_prefixed_array(Int32sl)
@lump_version(0)
def lump_hlpd(header, profile=None):
    return DetailPropLightStyle_t

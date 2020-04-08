from __future__ import division
from __future__ import absolute_import
from __future__ import print_function
from __future__ import unicode_literals
from future import standard_library
standard_library.install_aliases()

from construct import *	 # NOQA: #402


bsp_t = Struct(
    'ident' / Const(b'VBSP'),
)

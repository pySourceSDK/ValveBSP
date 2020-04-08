from __future__ import unicode_literals
from __future__ import division
from __future__ import absolute_import
from __future__ import print_function
from builtins import dict
from builtins import int
from builtins import range
from builtins import str
from builtins import open
from future import standard_library
standard_library.install_aliases()

from construct import *  # NOQA: E402
from .bsp_struct import *  # NOQA: E402


def BspParse(filename):
    bsp = Bsp()
    with open(filename, "rb") as f:
        try:
            results = bsp_t.parse_stream(f)
        except Exception as e:
            print(e)
    return bsp

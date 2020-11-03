from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals
from future import standard_library
standard_library.install_aliases()


class LumpUnsupportedError(Exception):
    pass


class LumpVersionUnsupportedError(Exception):
    pass


class LumpCompressedError(Exception):
    pass

[![GPLv3 license](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://github.com/pySourceSDK/ValveBSP/blob/master/LICENSE.txt)
[![PyPI pyversions](https://img.shields.io/pypi/pyversions/valvebsp.svg)](https://pypi.python.org/pypi/valvebsp/)
[![Platforms](https://img.shields.io/badge/platform-Linux,_MacOS,_Windows-blue)]()
[![PyPI version fury.io](https://badge.fury.io/py/valvebsp.svg)](https://pypi.python.org/pypi/valvebsp/)
[![GitHub Workflow Status (with event)](https://github.com/pySourceSDK/ValveBSP/actions/workflows/CI.yml/badge.svg)]()
[![Test coverage](https://github.com/pySourceSDK/ValveBSP/blob/master/docs/source/coverage.svg "coverage")]()

# ValveBSP

ValveBSP is a python library for parsing and editing .BSP asset files associated with Valve's Source engine. It provides provides access to lump data in map files.

Full documentation: https://pysourcesdk.github.io/ValveBSP/
<!--- start pypi omit -->

### Currently supported lumps

:heavy_check_mark: (52) Supported :x: (6) Unsupported :white_check_mark: (5) Unused :no_good: (1) will not support

| Lump # | Status             | Lump # | Status             | Lump # | Status             | Lump # | Status             |
| ---    | ---                | ---    | ---                | ---    | ---                | ---    | ---                |
| 0      | :heavy_check_mark: | 16     | :heavy_check_mark: | 32     | :white_check_mark: | 48     | :heavy_check_mark: |
| 1      | :heavy_check_mark: | 17     | :heavy_check_mark: | 33     | :heavy_check_mark: | 49     | :x:                |
| 2      | :heavy_check_mark: | 18     | :heavy_check_mark: | 34     | :heavy_check_mark: | 50     | :heavy_check_mark: |
| 3      | :heavy_check_mark: | 19     | :heavy_check_mark: | 35     | :heavy_check_mark: | 51     | :heavy_check_mark: |
| 4      | :x:                | 20     | :heavy_check_mark: | 36     | :heavy_check_mark: | 52     | :heavy_check_mark: |
| 5      | :heavy_check_mark: | 21     | :heavy_check_mark: | 37     | :heavy_check_mark: | 53     | :heavy_check_mark: |
| 6      | :heavy_check_mark: | 22     | :white_check_mark: | 38     | :heavy_check_mark: | 54     | :heavy_check_mark: |
| 7      | :heavy_check_mark: | 23     | :white_check_mark: | 39     | :heavy_check_mark: | 55     | :heavy_check_mark: |
| 8      | :heavy_check_mark: | 24     | :white_check_mark: | 40     | :heavy_check_mark: | 56     | :heavy_check_mark: |
| 9      | :heavy_check_mark: | 25     | :white_check_mark: | 41     | :heavy_check_mark: | 57     | :no_good:          |
| 10     | :heavy_check_mark: | 26     | :heavy_check_mark: | 42     | :heavy_check_mark: | 58     | :heavy_check_mark: |
| 11     | :heavy_check_mark: | 27     | :heavy_check_mark: | 43     | :heavy_check_mark: | 59     | :heavy_check_mark: |
| 12     | :heavy_check_mark: | 28     | :heavy_check_mark: | 44     | :heavy_check_mark: | 60     | :heavy_check_mark: |
| 13     | :heavy_check_mark: | 29     | :x:                | 45     | :heavy_check_mark: | 61     | :x:                |
| 14     | :heavy_check_mark: | 30     | :heavy_check_mark: | 46     | :heavy_check_mark: | 62     | :x:                |
| 15     | :heavy_check_mark: | 31     | :heavy_check_mark: | 47     | :heavy_check_mark: | 63     | :x:                |

<!--- end pypi omit -->
## Installation

### PyPI

ValveBSP is available on the Python Package Index. This makes installing it with pip as easy as:

```bash
pip3 install valvebsp
```

### Git

If you want the latest code or even feel like contributing, the code is available on GitHub.

You can easily clone the code with git:

```bash
git clone git@github.com:pySourceSDK/ValveBSP.git
```

and install it with:

```bash
python3 setup.py install
```

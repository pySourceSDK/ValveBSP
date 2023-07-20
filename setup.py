from setuptools import setup, find_packages

with open('README.md') as f:
    long_description = f.read()

VERSION = '{{VERSION_PLACEHOLDER}}'
if 'VERSION_PLACEHOLDER' in VERSION:
    VERSION = '0.0.0'

setup(
    name='valvebsp',
    packages=find_packages(exclude=["tests", "tests.*", '*docs*']),
    version=VERSION,
    description='A library to parse .bsp files (level files for the Source engine).',
    long_description=long_description,
    long_description_content_type="text/markdown",
    license='gpl-3.0',
    author='Maxime Dupuis',
    author_email='mdupuis@hotmail.ca',
    url='https://github.com/pySourceSDK/ValveBSP',
    keywords=['bsp', 'source', 'sourcesdk', 'hammer', 'valve'],
    install_requires=['construct', 'pyparsing', 'future'],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
    ],
)

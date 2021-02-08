from distutils.core import setup
setup(
    name='bsptools',
    packages=['bsptools', 'bsptools.structs'],
    version='0.0.1',
    license='gpl-3.0',
    description='A library to parse .bsp files used in the source engine.',
    author='Maxime Dupuis',
    author_email='mdupuis@hotmail.ca',
    url='https://maxdup.github.io/bsp-tools/',
    # download_url='https://github.com/maxdup/bsp-tools/archive/v0.0.1.tar.gz',
    keywords=['bsp', 'source', 'sourcesdk', 'hammer', 'valve'],
    install_requires=['construct', 'future'],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],
)

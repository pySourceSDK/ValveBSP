from distutils.core import setup
setup(
    name='valvebsp',
    packages=['valvebsp', 'valvebsp.structs'],
    version='1.0.0',
    license='gpl-3.0',
    description='A library to parse .bsp files used by the source engine.',
    author='Maxime Dupuis',
    author_email='mdupuis@hotmail.ca',
    url='https://github.com/pySourceSDK/ValveBSP',
    download_url='https://github.com/pySourceSDK/ValveBSP/archive/v1.0.0.tar.gz',
    keywords=['bsp', 'source', 'sourcesdk', 'hammer', 'valve'],
    install_requires=['construct', 'pyparsing', 'future'],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
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

from distutils.core import setup
import sys, os
import py2exe

py2exe_options = dict(
    #packages=pkglist,
    #includes=['_pkglist'],
    excludes=['_ssl',  # Exclude _ssl
              'pyreadline', 'difflib', 'doctest', 'locale',
              'optparse', 'pickle', 'calendar'],  # Exclude standard library
    dll_excludes=['msvcr71.dll', "w9xpopen.exe"],  # Exclude msvcr71
    compressed=True,  # Compress library.zip
    bundle_files=1,
    #dist_dir="..",
    optimize=2,
    )

setup(console=["cmt.py"], 
        zipfile=None,
        options={'py2exe': py2exe_options},
        windows=[{
            'script': "cmt.py",
           # 'uac_info': "requireAdministrator"
            }],
            )

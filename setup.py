__author__ = 'ktussey'
from setuptools import find_packages
from distutils.core import setup
from __version__ import __version__
import py2exe


class Target:
    def __init__(self, **kw):
        self.__dict__.update(kw)

target = Target(
    product_name='WhoIsMissing',
    description='A utility for examining ASCENT sequence files and displaying the missing injections.',
    script='WhoIsMissing.py',
    dest_base='WhoIsMissing',
    version=__version__,
    company_name='Whereskenneth Free Software',
    copyright='',
    name='Whereskenneth.WhoIsMissing'
)

setup(name='WhoIsMissing',
      author='Kenneth Tussey',
      author_email='whereskenneth@gmail.com',
      version=__version__,
      description='A utility for examining ASCENT sequence files and displaying the missing injections.',
      packages=find_packages(),
      requires=['behave', 'py2exe'],
      options={'py2exe': {'bundle_files': 1, 'compressed': True}},
      console=[target],
      zipfile=None,
)

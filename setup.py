#from ez_setup import use_setuptools
#use_setuptools()
from setuptools import setup, find_packages

setup(# package information
      name="myExamplePackage",
      version="0.0.1dev",
      description='Simple repo setup to check documentation',
      long_description=''' ''',
      # What code to include as packages
      packages=['myexpackage'],
      # What data to include as packages
      include_package_data=True,
      package_data={'': ['data/*.dat']}
      )

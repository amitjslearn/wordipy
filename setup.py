# FEW THINGS ARE IMPORTED BUT WILL BE USED LATER
# import io
# import os
# import sys
# from shutil import rmtree
from setuptools import find_packages, setup, Command

with open("README.md", 'r') as f:
    long_description = f.read()

setup(name='wordipy',
      version='0.1',
      description='wordipy is dummy  package which can be used in preprocessing for NLP',
      py_modules=['wordipy'],
      install_requires=[
          'word2number', 'nltk',
      ],
	packages = find_packages(where='.'),
      #package_dir = {'': 'lib'}
      )

# python3 setup.py sdist bdist_wheel

import io
import os
import sys
from shutil import rmtree

from setuptools import find_packages, setup, Command
setup(name='wordipy',
      version='0.1',
      description='wordipy is dummy  package which can be used in preprocessing for NLP',
      py_modules=['wordipy'],
      install_requires=[
         'word2number', 'nltk', 
      ],      
      #package_dir = {'': 'lib'}
      )

#!/usr/bin/env python

from setuptools import setup, find_packages

# This import leads to ambiquity
# 
# Rather use:
# 
# Assume structure:
# Code/Source/folder0/__ini__.py (package 'folder0')
#
# Replace:
# packages = ['folder0']
# package_dir={'':'Code/Source'}
# 
## 

setup(name='project',
      version='0.0.1',
      description='Some description for the project',
      author='firstname surname',
      author_email='firstname.surname@fau.de',
      url='https://<server>/<path-to-project>',
      packages=find_packages('Code/Source'),
      package_dir={'':'Code/Source'}
     )

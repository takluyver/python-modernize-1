from __future__ import absolute_import
import os, re
from setuptools import setup

module_file = open(os.path.join(os.path.dirname(__file__), 'libmodernize', '__init__.py'), 'r').read()
version_match = re.search(r"__version__ = ['\"]([^'\"]*)['\"]", module_file, re.M)
if not version_match:
    raise Exception("couldn't find version number")
version = version_match.group(1)

setup(version=version, test_suite='nose.collector')

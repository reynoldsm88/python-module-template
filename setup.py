#!/usr/bin/env python3

from setuptools import setup, find_packages

setup( name = 'stuff-tf-word-embeddings',
       version = '1.0',
       py_modules = [ 'stuff-tf-word-embeddings' ],
       packages = find_packages( exclude = ("docs", "tests") ),
       test_suite = "tests",
       tests_require = [ 'nose' ] )
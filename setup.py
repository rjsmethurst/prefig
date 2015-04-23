#!/usr/bin/env python

from setuptools import setup

setup(
    name="prefig",
    version="0.1",
    author="Becky Smethurst",
    py_modules=['prefig'],
    #entry_points = {
     #   'console_scripts': ['prefig = prefig:Prefig']
     #   }
    scripts=['prefig.py']
      )

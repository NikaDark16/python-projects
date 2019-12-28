#!/usr/bin/env python

from distutils.core import setup

setup(name='rikaset',
      version='4',
      description='It\'s program for working with sets',
      author='IceArrow256',
      author_email='icearrow256@gmail.com',
      packages=['rikaset'],
      entry_points={'console_scripts': ['rikaset=rikaset.main:main']},
      requires=['PyQt5', 'matplotlib-venn', 'matplotlib']
      )

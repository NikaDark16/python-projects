#!/usr/bin/env python

from distutils.core import setup

setup(name='mitsuscreenshots',
      version='4',
      description='It\'s program for sorting and collecting screenshots',
      author='IceArrow256',
      author_email='icearrow256@gmail.com',
      packages=['mitsuscreenshots'],
      entry_points={'console_scripts': ['mitsuscreenshots=mitsuscreenshots.main:main']},
      requires=['PyQt5', 'ia256utilities', 'pyxdg']
      )

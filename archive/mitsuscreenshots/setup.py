#!/usr/bin/env python

from distutils.core import setup

setup(name='MitsuScreenshots',
      version='4',
      description='It\'s program for sorting and collecting screenshots',
      author='IceArrow256',
      author_email='icearrow256@gmail.com',
      url='https://github.com/IceArrow256/MitsuScreenshots',
      packages=['mitsuscreenshots'],
      entry_points={'console_scripts': ['mitsuscreenshots=mitsuscreenshots.main:main']},
      requires=['PyQt5', 'ia256utilities', 'pyxdg']
      )

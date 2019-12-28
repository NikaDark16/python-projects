#!/usr/bin/env python

from distutils.core import setup

setup(name='sayaset',
      version='4',
      description='It\'s program for working with sets',
      author='IceArrow256',
      author_email='icearrow256@gmail.com',
      packages=['sayaset'],
      entry_points={'console_scripts': ['SayaSet=sayaset.main:main']},
      requires=['PyQt5']
      )

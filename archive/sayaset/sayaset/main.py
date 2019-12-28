# !/usr/bin/python
# -*- coding: utf-8 -*-

import argparse

import sayaset.gui as gui

__author__ = "IceArrow256"
__version__ = '4'


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-V', '--version', help='show program\'s version number and exit', action='store_true')
    args = parser.parse_args()

    if args.version:
        print("RikaSet ({})".format(__version__))
    else:
        gui.main()


if __name__ == '__main__':
    main()

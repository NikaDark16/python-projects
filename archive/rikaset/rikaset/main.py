# !/usr/bin/python
# -*- coding: utf-8 -*-

import argparse

import rikaset.cli as cli
import rikaset.gui as gui

__author__ = "IceArrow256"
__version__ = '4'


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-V', '--version', help='show program\'s version number and exit', action='store_true')
    parser.add_argument('--cli', help='launch the RikaSet CLI', action='store_true')
    args = parser.parse_args()

    if args.version:
        print("RikaSet ({})".format(__version__))
    elif args.cli:
        cli.main()
    else:
        gui.main()


if __name__ == '__main__':
    main()

# !/usr/bin/python
# -*- coding: utf-8 -*-

import argparse

import mitsuscreenshots.cli as cli
import mitsuscreenshots.gui as gui
import mitsuscreenshots.organize as organize

__author__ = "IceArrow256"
__version__ = '3'


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-c', '--config', help='show program\'s config path and exit', action='store_true')
    parser.add_argument('-V', '--version', help='show program\'s version number and exit', action='store_true')
    parser.add_argument('--gui', help='launch the MitsuScreenshots GUI', action='store_true')
    args = parser.parse_args()

    if args.version:
        print("MitsuScreenshots ({})".format(__version__))
    elif args.config:
        print("MitsuScreenshots config path: " + organize.get_config_path())
    elif args.gui:
        gui.main()
    else:
        cli.main()


if __name__ == '__main__':
    main()

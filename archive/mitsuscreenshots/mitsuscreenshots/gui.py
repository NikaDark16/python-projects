import sys

import PyQt5.QtWidgets as W

import mitsuscreenshots.mainwindow as mw

__author__ = "IceArrow256"
__version__ = '2'


def main():
    app = W.QApplication([])
    application = mw.MainWindow()
    application.show()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()

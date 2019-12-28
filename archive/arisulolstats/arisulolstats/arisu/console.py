__author__ = 'IceArrow256'

import PyQt5.QtCore as C
import PyQt5.QtGui as G
import PyQt5.QtWidgets as W


class Console(W.QPlainTextEdit):
    signal_write = C.pyqtSignal(str)

    def __init__(self, parent):
        super(Console, self).__init__(parent)

        self.init()

    def init(self):
        self.setReadOnly(True)
        self.signal_write.connect(self._write)

    def write(self, string):
        self.signal_write.emit(string)

    def write_line(self, string):
        self.signal_write.emit(string + "\n")

    @C.pyqtSlot(str)
    def _write(self, string):
        print(string, end='')
        self.moveCursor(G.QTextCursor.End)
        self.insertPlainText(string)

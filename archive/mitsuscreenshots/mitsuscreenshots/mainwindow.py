import PyQt5.QtCore as C
import PyQt5.QtGui as G
import PyQt5.QtWidgets as W

import mitsuscreenshots.organize as organize
import mitsuscreenshots.uimainwindow as uimw

__author__ = "IceArrow256"
__version__ = '4'


class ConsoleHandler(C.QObject):
    signal_print = C.pyqtSignal(str)

    def __init__(self, console: W.QPlainTextEdit):
        super(ConsoleHandler, self).__init__()

        self.console = console

        self.console.setReadOnly(True)
        self.signal_print.connect(self._print)

    def print(self, string):
        self.signal_print.emit(string)

    def println(self, string):
        self.signal_print.emit(string + "\n")

    @C.pyqtSlot(str)
    def _print(self, string):
        print(string, end='')
        self.console.moveCursor(G.QTextCursor.End)
        self.console.insertPlainText(string)


class MainWindow(W.QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = uimw.Ui_MainWindow()
        self.ui.setupUi(self)

        self.console_handler = ConsoleHandler(self.ui.plainTextEditConsole)

        self.screenshots_path = organize.get_screenshots_path()
        self.unsorted_path = organize.get_unsorted_path()

        self.ui.pushButtonProcessScreenshots.clicked.connect(self.press_button_process_screenshots)
        self.ui.pushButtonBrowseScreenshots.clicked.connect(self.press_button_browse_screenshots)
        self.ui.pushButtonBrowseUnsorted.clicked.connect(self.press_button_browse_unsorted)

        self.center()

    def __del__(self):
        organize.keep_screenshots_path(self.screenshots_path)
        organize.keep_unsorted_path(self.unsorted_path)

    @property
    def screenshots_path(self):
        """
        :rtype: str
        """
        return self.ui.lineEditScreenshotsPath.text()

    @screenshots_path.setter
    def screenshots_path(self, value: str):
        self.ui.lineEditScreenshotsPath.setText(value)

    @property
    def unsorted_path(self):
        """
        :rtype: str
        """
        return self.ui.lineEditUnsortedPath.text()

    @unsorted_path.setter
    def unsorted_path(self, value: str):
        self.ui.lineEditUnsortedPath.setText(value)

    def press_button_process_screenshots(self):
        for line in organize.organize_screenshots():
            self.console_handler.println(line)

    def press_button_browse_screenshots(self):
        new_path = W.QFileDialog.getExistingDirectory(None, 'Select a screenshots folder:', self.screenshots_path,
                                                      W.QFileDialog.ShowDirsOnly)
        if new_path:
            self.screenshots_path = new_path

    def press_button_browse_unsorted(self):
        new_path = W.QFileDialog.getExistingDirectory(None, 'Select a unsorted folder:', self.unsorted_path,
                                                      W.QFileDialog.ShowDirsOnly)
        if new_path:
            self.screenshots_path = new_path

    def center(self):
        qr = self.frameGeometry()
        cp = W.QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

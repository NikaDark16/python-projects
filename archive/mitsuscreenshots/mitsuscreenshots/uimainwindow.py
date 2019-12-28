# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'uimainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1280, 720)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.labelScreenshotsPath = QtWidgets.QLabel(self.centralwidget)
        self.labelScreenshotsPath.setObjectName("labelScreenshotsPath")
        self.gridLayout.addWidget(self.labelScreenshotsPath, 1, 0, 1, 1)
        self.labelUnsortedPath = QtWidgets.QLabel(self.centralwidget)
        self.labelUnsortedPath.setObjectName("labelUnsortedPath")
        self.gridLayout.addWidget(self.labelUnsortedPath, 2, 0, 1, 1)
        self.lineEditUnsortedPath = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEditUnsortedPath.setObjectName("lineEditUnsortedPath")
        self.gridLayout.addWidget(self.lineEditUnsortedPath, 2, 1, 1, 1)
        self.lineEditScreenshotsPath = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEditScreenshotsPath.setObjectName("lineEditScreenshotsPath")
        self.gridLayout.addWidget(self.lineEditScreenshotsPath, 1, 1, 1, 1)
        self.pushButtonBrowseScreenshots = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonBrowseScreenshots.setObjectName("pushButtonBrowseScreenshots")
        self.gridLayout.addWidget(self.pushButtonBrowseScreenshots, 1, 2, 1, 1)
        self.pushButtonBrowseUnsorted = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonBrowseUnsorted.setObjectName("pushButtonBrowseUnsorted")
        self.gridLayout.addWidget(self.pushButtonBrowseUnsorted, 2, 2, 1, 1)
        self.plainTextEditConsole = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.plainTextEditConsole.setObjectName("plainTextEditConsole")
        self.gridLayout.addWidget(self.plainTextEditConsole, 0, 0, 1, 3)
        self.pushButtonProcessScreenshots = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonProcessScreenshots.setObjectName("pushButtonProcessScreenshots")
        self.gridLayout.addWidget(self.pushButtonProcessScreenshots, 3, 0, 1, 3)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MitsuScreenshots"))
        self.labelScreenshotsPath.setText(_translate("MainWindow", "Screenshots folder:"))
        self.labelUnsortedPath.setText(_translate("MainWindow", "Unsorted folder:"))
        self.pushButtonBrowseScreenshots.setText(_translate("MainWindow", "Browse..."))
        self.pushButtonBrowseUnsorted.setText(_translate("MainWindow", "Browse..."))
        self.pushButtonProcessScreenshots.setText(_translate("MainWindow", "Process screenshots"))

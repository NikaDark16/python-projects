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
        MainWindow.resize(531, 678)
        MainWindow.setMinimumSize(QtCore.QSize(0, 0))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.labelExpression = QtWidgets.QLabel(self.centralwidget)
        self.labelExpression.setObjectName("labelExpression")
        self.gridLayout.addWidget(self.labelExpression, 0, 0, 1, 1)
        self.pushButtonSetSets = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonSetSets.setObjectName("pushButtonSetSets")
        self.gridLayout.addWidget(self.pushButtonSetSets, 2, 0, 1, 2)
        self.gridLayoutInput = QtWidgets.QGridLayout()
        self.gridLayoutInput.setObjectName("gridLayoutInput")
        self.labelStep = QtWidgets.QLabel(self.centralwidget)
        self.labelStep.setObjectName("labelStep")
        self.gridLayoutInput.addWidget(self.labelStep, 1, 2, 1, 1)
        self.pushButtonBack = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonBack.setObjectName("pushButtonBack")
        self.gridLayoutInput.addWidget(self.pushButtonBack, 1, 1, 1, 1)
        self.labelSets = QtWidgets.QLabel(self.centralwidget)
        self.labelSets.setText("")
        self.labelSets.setObjectName("labelSets")
        self.gridLayoutInput.addWidget(self.labelSets, 5, 1, 1, 3)
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustIgnored)
        self.tableWidget.setShowGrid(True)
        self.tableWidget.setRowCount(1)
        self.tableWidget.setColumnCount(1)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.horizontalHeader().setVisible(False)
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(False)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(500)
        self.tableWidget.horizontalHeader().setHighlightSections(False)
        self.tableWidget.horizontalHeader().setMinimumSectionSize(500)
        self.tableWidget.verticalHeader().setVisible(False)
        self.tableWidget.verticalHeader().setDefaultSectionSize(350)
        self.tableWidget.verticalHeader().setMinimumSectionSize(350)
        self.gridLayoutInput.addWidget(self.tableWidget, 7, 1, 1, 3)
        self.pushButtonNext = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonNext.setObjectName("pushButtonNext")
        self.gridLayoutInput.addWidget(self.pushButtonNext, 1, 3, 1, 1)
        self.labelName = QtWidgets.QLabel(self.centralwidget)
        self.labelName.setText("")
        self.labelName.setObjectName("labelName")
        self.gridLayoutInput.addWidget(self.labelName, 4, 1, 1, 3)
        self.labelResult = QtWidgets.QLabel(self.centralwidget)
        self.labelResult.setText("")
        self.labelResult.setObjectName("labelResult")
        self.gridLayoutInput.addWidget(self.labelResult, 6, 1, 1, 3)
        self.gridLayout.addLayout(self.gridLayoutInput, 3, 0, 1, 2)
        self.gridLayoutSets = QtWidgets.QGridLayout()
        self.gridLayoutSets.setObjectName("gridLayoutSets")
        self.gridLayout.addLayout(self.gridLayoutSets, 1, 0, 1, 2)
        self.pushButtonSolve = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonSolve.setObjectName("pushButtonSolve")
        self.gridLayout.addWidget(self.pushButtonSolve, 6, 0, 1, 3)
        self.lineEditExpression = QtWidgets.QLineEdit(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEditExpression.sizePolicy().hasHeightForWidth())
        self.lineEditExpression.setSizePolicy(sizePolicy)
        self.lineEditExpression.setObjectName("lineEditExpression")
        self.gridLayout.addWidget(self.lineEditExpression, 0, 1, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "RikaSet"))
        self.labelExpression.setText(_translate("MainWindow", "Expression:"))
        self.pushButtonSetSets.setText(_translate("MainWindow", "Set sets"))
        self.labelStep.setText(_translate("MainWindow", "Step"))
        self.pushButtonBack.setText(_translate("MainWindow", "<"))
        self.pushButtonNext.setText(_translate("MainWindow", ">"))
        self.pushButtonSolve.setText(_translate("MainWindow", "Solve"))

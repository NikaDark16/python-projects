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
        MainWindow.resize(1081, 623)
        MainWindow.setMinimumSize(QtCore.QSize(0, 0))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.lineEditRatioAB = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEditRatioAB.setReadOnly(True)
        self.lineEditRatioAB.setObjectName("lineEditRatioAB")
        self.gridLayout_2.addWidget(self.lineEditRatioAB, 1, 4, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setObjectName("label_6")
        self.gridLayout_2.addWidget(self.label_6, 1, 0, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_7.sizePolicy().hasHeightForWidth())
        self.label_7.setSizePolicy(sizePolicy)
        self.label_7.setObjectName("label_7")
        self.gridLayout_2.addWidget(self.label_7, 3, 0, 1, 1)
        self.lineEditRatioA = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEditRatioA.setObjectName("lineEditRatioA")
        self.gridLayout_2.addWidget(self.lineEditRatioA, 1, 1, 1, 1)
        self.lineEditRatioP = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEditRatioP.setReadOnly(True)
        self.lineEditRatioP.setObjectName("lineEditRatioP")
        self.gridLayout_2.addWidget(self.lineEditRatioP, 6, 4, 1, 1)
        self.lineEditRatioB = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEditRatioB.setObjectName("lineEditRatioB")
        self.gridLayout_2.addWidget(self.lineEditRatioB, 3, 1, 1, 1)
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setObjectName("label_10")
        self.gridLayout_2.addWidget(self.label_10, 3, 2, 1, 2)
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setObjectName("label_9")
        self.gridLayout_2.addWidget(self.label_9, 1, 2, 1, 2)
        self.lineEditRatioAA = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEditRatioAA.setReadOnly(True)
        self.lineEditRatioAA.setObjectName("lineEditRatioAA")
        self.gridLayout_2.addWidget(self.lineEditRatioAA, 4, 4, 1, 1)
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_11.setObjectName("label_11")
        self.gridLayout_2.addWidget(self.label_11, 4, 2, 1, 2)
        self.label_12 = QtWidgets.QLabel(self.centralwidget)
        self.label_12.setObjectName("label_12")
        self.gridLayout_2.addWidget(self.label_12, 5, 2, 1, 2)
        self.lineEditRatioBA = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEditRatioBA.setReadOnly(True)
        self.lineEditRatioBA.setObjectName("lineEditRatioBA")
        self.gridLayout_2.addWidget(self.lineEditRatioBA, 3, 4, 1, 1)
        self.lineEditRatioBB = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEditRatioBB.setReadOnly(True)
        self.lineEditRatioBB.setObjectName("lineEditRatioBB")
        self.gridLayout_2.addWidget(self.lineEditRatioBB, 5, 4, 1, 1)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.gridLayout_2.addWidget(self.label, 0, 0, 1, 5)
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setObjectName("label_8")
        self.gridLayout_2.addWidget(self.label_8, 6, 2, 1, 2)
        self.verticalLayout.addLayout(self.gridLayout_2)
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.label_19 = QtWidgets.QLabel(self.centralwidget)
        self.label_19.setObjectName("label_19")
        self.gridLayout_3.addWidget(self.label_19, 1, 2, 1, 1)
        self.lineEditCompositionP = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEditCompositionP.setObjectName("lineEditCompositionP")
        self.gridLayout_3.addWidget(self.lineEditCompositionP, 1, 1, 1, 1)
        self.lineEditComposition = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEditComposition.setReadOnly(True)
        self.lineEditComposition.setObjectName("lineEditComposition")
        self.gridLayout_3.addWidget(self.lineEditComposition, 1, 3, 1, 1)
        self.lineEditCompositionQ = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEditCompositionQ.setObjectName("lineEditCompositionQ")
        self.gridLayout_3.addWidget(self.lineEditCompositionQ, 2, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setObjectName("label_2")
        self.gridLayout_3.addWidget(self.label_2, 0, 0, 1, 4)
        self.label_15 = QtWidgets.QLabel(self.centralwidget)
        self.label_15.setObjectName("label_15")
        self.gridLayout_3.addWidget(self.label_15, 1, 0, 1, 1)
        self.label_17 = QtWidgets.QLabel(self.centralwidget)
        self.label_17.setObjectName("label_17")
        self.gridLayout_3.addWidget(self.label_17, 2, 0, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout_3)
        self.gridLayout_7 = QtWidgets.QGridLayout()
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.label_16 = QtWidgets.QLabel(self.centralwidget)
        self.label_16.setObjectName("label_16")
        self.gridLayout_7.addWidget(self.label_16, 2, 0, 1, 1)
        self.label_14 = QtWidgets.QLabel(self.centralwidget)
        self.label_14.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_14.setObjectName("label_14")
        self.gridLayout_7.addWidget(self.label_14, 1, 0, 1, 1)
        self.lineEditPr1 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEditPr1.setObjectName("lineEditPr1")
        self.gridLayout_7.addWidget(self.lineEditPr1, 2, 1, 1, 1)
        self.lineEditPr2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEditPr2.setObjectName("lineEditPr2")
        self.gridLayout_7.addWidget(self.lineEditPr2, 3, 1, 1, 1)
        self.label_13 = QtWidgets.QLabel(self.centralwidget)
        self.label_13.setObjectName("label_13")
        self.gridLayout_7.addWidget(self.label_13, 0, 0, 1, 2)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_7.addItem(spacerItem, 6, 0, 1, 2)
        self.lineEditProjectionA = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEditProjectionA.setObjectName("lineEditProjectionA")
        self.gridLayout_7.addWidget(self.lineEditProjectionA, 1, 1, 1, 1)
        self.lineEditPr12 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEditPr12.setObjectName("lineEditPr12")
        self.gridLayout_7.addWidget(self.lineEditPr12, 4, 1, 1, 1)
        self.label_18 = QtWidgets.QLabel(self.centralwidget)
        self.label_18.setObjectName("label_18")
        self.gridLayout_7.addWidget(self.label_18, 3, 0, 1, 1)
        self.label_20 = QtWidgets.QLabel(self.centralwidget)
        self.label_20.setObjectName("label_20")
        self.gridLayout_7.addWidget(self.label_20, 4, 0, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout_7)
        self.gridLayout.addLayout(self.verticalLayout, 4, 0, 1, 1)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.gridLayout_6 = QtWidgets.QGridLayout()
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setObjectName("label_5")
        self.gridLayout_6.addWidget(self.label_5, 0, 0, 1, 2)
        self.lineEditSubSettingA = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEditSubSettingA.setObjectName("lineEditSubSettingA")
        self.gridLayout_6.addWidget(self.lineEditSubSettingA, 1, 1, 1, 1)
        self.label_22 = QtWidgets.QLabel(self.centralwidget)
        self.label_22.setObjectName("label_22")
        self.gridLayout_6.addWidget(self.label_22, 1, 0, 1, 1)
        self.labelSubSets = QtWidgets.QLabel(self.centralwidget)
        self.labelSubSets.setText("")
        self.labelSubSets.setObjectName("labelSubSets")
        self.gridLayout_6.addWidget(self.labelSubSets, 2, 0, 1, 2)
        self.verticalLayout_2.addLayout(self.gridLayout_6)
        self.gridLayout_5 = QtWidgets.QGridLayout()
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.label_24 = QtWidgets.QLabel(self.centralwidget)
        self.label_24.setObjectName("label_24")
        self.gridLayout_5.addWidget(self.label_24, 2, 0, 1, 1)
        self.lineEditAddition = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEditAddition.setReadOnly(True)
        self.lineEditAddition.setObjectName("lineEditAddition")
        self.gridLayout_5.addWidget(self.lineEditAddition, 1, 3, 1, 1)
        self.label_23 = QtWidgets.QLabel(self.centralwidget)
        self.label_23.setObjectName("label_23")
        self.gridLayout_5.addWidget(self.label_23, 1, 0, 1, 1)
        self.lineEditAdditionA = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEditAdditionA.setObjectName("lineEditAdditionA")
        self.gridLayout_5.addWidget(self.lineEditAdditionA, 1, 1, 1, 1)
        self.lineEditAdditionB = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEditAdditionB.setObjectName("lineEditAdditionB")
        self.gridLayout_5.addWidget(self.lineEditAdditionB, 2, 1, 1, 1)
        self.label_25 = QtWidgets.QLabel(self.centralwidget)
        self.label_25.setObjectName("label_25")
        self.gridLayout_5.addWidget(self.label_25, 1, 2, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setObjectName("label_4")
        self.gridLayout_5.addWidget(self.label_4, 0, 0, 1, 4)
        self.verticalLayout_2.addLayout(self.gridLayout_5)
        self.gridLayout_4 = QtWidgets.QGridLayout()
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.label_27 = QtWidgets.QLabel(self.centralwidget)
        self.label_27.setObjectName("label_27")
        self.gridLayout_4.addWidget(self.label_27, 2, 0, 1, 1)
        self.lineEditCartesian = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEditCartesian.setReadOnly(True)
        self.lineEditCartesian.setObjectName("lineEditCartesian")
        self.gridLayout_4.addWidget(self.lineEditCartesian, 1, 3, 1, 1)
        self.lineEditCartesianB = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEditCartesianB.setObjectName("lineEditCartesianB")
        self.gridLayout_4.addWidget(self.lineEditCartesianB, 2, 1, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setObjectName("label_3")
        self.gridLayout_4.addWidget(self.label_3, 0, 0, 1, 4)
        self.label_26 = QtWidgets.QLabel(self.centralwidget)
        self.label_26.setObjectName("label_26")
        self.gridLayout_4.addWidget(self.label_26, 1, 0, 1, 1)
        self.label_28 = QtWidgets.QLabel(self.centralwidget)
        self.label_28.setObjectName("label_28")
        self.gridLayout_4.addWidget(self.label_28, 1, 2, 1, 1)
        self.lineEditCartesianA = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEditCartesianA.setObjectName("lineEditCartesianA")
        self.gridLayout_4.addWidget(self.lineEditCartesianA, 1, 1, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_4.addItem(spacerItem1, 3, 0, 1, 4)
        self.verticalLayout_2.addLayout(self.gridLayout_4)
        self.gridLayout.addLayout(self.verticalLayout_2, 4, 1, 1, 1)
        self.pushButtonSolveAll = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonSolveAll.setObjectName("pushButtonSolveAll")
        self.gridLayout.addWidget(self.pushButtonSolveAll, 7, 0, 1, 2)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "SayaSet"))
        self.label_6.setText(_translate("MainWindow", "A"))
        self.label_7.setText(_translate("MainWindow", "B"))
        self.lineEditRatioA.setText(_translate("MainWindow", "1, 2, 3"))
        self.lineEditRatioB.setText(_translate("MainWindow", "\"a\", \"b\", \"c\""))
        self.label_10.setText(_translate("MainWindow", "BxA"))
        self.label_9.setText(_translate("MainWindow", "AxB"))
        self.label_11.setText(_translate("MainWindow", "AxA"))
        self.label_12.setText(_translate("MainWindow", "BxB"))
        self.label.setText(_translate("MainWindow", "Ratio"))
        self.label_8.setText(_translate("MainWindow", "Random P"))
        self.label_19.setText(_translate("MainWindow", "P○Q"))
        self.lineEditCompositionP.setText(_translate("MainWindow", "(1, \"a\"), (1, \"b\"), (3, \"c\")"))
        self.lineEditCompositionQ.setText(_translate("MainWindow", "(\"a\", 4), (\"a\", \"w\"), (\"b\", \"v\"), (\"b\", \"x\")"))
        self.label_2.setText(_translate("MainWindow", "Composition"))
        self.label_15.setText(_translate("MainWindow", "P"))
        self.label_17.setText(_translate("MainWindow", "Q"))
        self.label_16.setText(_translate("MainWindow", "Pr1"))
        self.label_14.setText(_translate("MainWindow", "A"))
        self.label_13.setText(_translate("MainWindow", "Projection"))
        self.lineEditProjectionA.setText(_translate("MainWindow", "(1, 2, 3, 4), (5, 3, 7), (4, 7, 8, 9) "))
        self.label_18.setText(_translate("MainWindow", "Pr2"))
        self.label_20.setText(_translate("MainWindow", "Pr12"))
        self.label_5.setText(_translate("MainWindow", "SubSetting"))
        self.lineEditSubSettingA.setText(_translate("MainWindow", "1, 5, 6, 7, 8, 9, 33"))
        self.label_22.setText(_translate("MainWindow", "A"))
        self.label_24.setText(_translate("MainWindow", "B"))
        self.label_23.setText(_translate("MainWindow", "A"))
        self.lineEditAdditionA.setText(_translate("MainWindow", "(1, 2,), (3, 4), (5,6), (7, 8, 9)"))
        self.lineEditAdditionB.setText(_translate("MainWindow", "(1, 6), (2, 3), (4, 5), (7, 8), (9)"))
        self.label_25.setText(_translate("MainWindow", "A+ B"))
        self.label_4.setText(_translate("MainWindow", "Addition"))
        self.label_27.setText(_translate("MainWindow", "B"))
        self.lineEditCartesianB.setText(_translate("MainWindow", "\"a\", \"b\", \"c\""))
        self.label_3.setText(_translate("MainWindow", "Cartesian Multiplication"))
        self.label_26.setText(_translate("MainWindow", "A"))
        self.label_28.setText(_translate("MainWindow", "AxB"))
        self.lineEditCartesianA.setText(_translate("MainWindow", "1, 2, 3"))
        self.pushButtonSolveAll.setText(_translate("MainWindow", "Solve all"))

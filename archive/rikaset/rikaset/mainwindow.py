import PyQt5.QtWidgets as W
import matplotlib.backends.backend_qt5agg as BQ5
import matplotlib.pyplot as PP
import matplotlib_venn as V

import rikaset.set as S
import rikaset.setscalculator as SC
import rikaset.uimainwindow as UMW

__author__ = "IceArrow256"
__version__ = '4'


class VennDiagram(BQ5.FigureCanvasQTAgg):
    def __init__(self, set_labels=[]):
        self.figure = PP.figure()
        super().__init__(self.figure)
        if len(set_labels) == 2:
            self.ids = ["10", "01", "11"]
            self.venn = V.venn2(subsets=(1, 1, 1),
                                set_labels=set_labels,
                                subset_label_formatter=lambda x: "",
                                set_colors=['white', 'white', 'white'])
            V.venn2_circles(subsets=(1, 1, 1))
        elif len(set_labels) == 3:
            self.ids = ["100", "010", "001", "110", "101", "011", "111"]
            self.venn = V.venn3(subsets=(1, 1, 1, 1, 1, 1, 1),
                                set_labels=set_labels,
                                subset_label_formatter=lambda x: "",
                                set_colors=['white', 'white', 'white', 'white', 'white', 'white', 'white'])
            V.venn3_circles(subsets=(1, 1, 1, 1, 1, 1, 1))
        else:
            raise ValueError()

    def clear(self):
        for i in self.ids:
            self.venn.get_patch_by_id(i).set_color('white')
        self.draw()

    def set(self, set_of_ids):
        self.clear()
        for i in set_of_ids:
            try:
                self.venn.get_patch_by_id(i).set_color('black')
            except IndexError:
                self.venn.get_patch_by_id(i[:2]).set_color('black')
        self.draw()

    def __del__(self):
        self.figure.clear()


class MainWindow(W.QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = UMW.Ui_MainWindow()
        self.ui.setupUi(self)
        self.center()

        self.step = 0

        self.venn_diagram = None

        msg = W.QMessageBox()
        msg.setIcon(W.QMessageBox.Information)
        msg.setText("Выражение вводиться в поле Expression, где используеться символы: "
                    "'u' - объединение, 'n' - пересечение, '\\' - разность, '+' - симметрическая разность, "
                    "'_' - дополнение. Большие буквы являются названиями "
                    "множеств. Чтобы задать множества, нужно нажать 'Sets sets'. Мнжества задаются "
                    "в виде '1 2 b a 4' (без скобочек). Чтобы решить множество нужно нажать 'Solve'. "
                    "Круги Эйлера рисуються только при условии, что множест 2 или 3.")
        msg.setInformativeText("Пример\n"
                               "Expression: An_B\\_(C+B)\n"
                               "A: 1 2 3\n"
                               "B: 3 4 5\n"
                               "C: 4 3 2\n")
        msg.setWindowTitle("Важно")
        msg.setStandardButtons(W.QMessageBox.Ok)

        retval = msg.exec_()

        self.expr = SC.SetsCalculator("")
        self.sets_label = {}
        self.sets_input = {}

        self.ui.pushButtonSetSets.clicked.connect(self.pressSetSets)
        self.ui.pushButtonSolve.clicked.connect(self.pressSolve)
        self.ui.pushButtonNext.clicked.connect(self.pressNext)
        self.ui.pushButtonBack.clicked.connect(self.pressBack)

    def pressSetSets(self):
        self.expr.input = self.ui.lineEditExpression.text().replace(' ', '')
        for name in self.sets_label:
            if name not in self.expr.sets:
                self.ui.gridLayoutSets.removeWidget(self.sets_label[name])
                self.ui.gridLayoutSets.removeWidget(self.sets_input[name])
                try:
                    self.sets_label[name].deleteLater()
                    self.sets_input[name].deleteLater()
                except AttributeError:
                    pass
                self.sets_label[name] = None
                self.sets_input[name] = None
        for name in list(self.sets_label):
            if self.sets_label[name] is None:
                del self.sets_label[name]
                del self.sets_input[name]
        if self.expr.sets:
            for name in self.expr.sets:
                if name not in self.sets_label:
                    self.sets_label[name] = W.QLabel(name + ":", self.ui.centralwidget)
                    self.sets_input[name] = W.QLineEdit(self.ui.centralwidget)
                    i = 1
                    while True:
                        if self.ui.gridLayoutSets.itemAtPosition(i, 0) is None:
                            self.ui.gridLayoutSets.addWidget(self.sets_label[name], i, 0)
                            self.ui.gridLayoutSets.addWidget(self.sets_input[name], i, 1)
                            break
                        i += 1

    def pressSolve(self):
        self.pressSetSets()
        self.expr.input = self.ui.lineEditExpression.text().replace(' ', '')
        self.expr.iter = 0
        self.expr.current_operation = 1
        sets = {}
        venn_num = 1
        for name in self.expr.sets:
            if len(self.sets_label) == 3 or len(self.sets_label) == 2:
                sets[name] = S.Set(name, set(self.sets_input[name].text().split(" ")), venn_num)
                venn_num += 1
            else:
                sets[name] = S.Set(name, set(self.sets_input[name].text().split(" ")), venn_num)
        self.expr.sets = sets
        try:
            result = self.expr.execute()
            self.step = 0
            self.ui.labelStep.setText("Step " + str(self.step + 1))
            self.ui.labelName.setText(self.expr.solution[self.step]["n"])
            self.ui.labelSets.setText(self.expr.solution[self.step]["s"])
            self.ui.labelResult.setText(self.expr.solution[self.step]["r"])
            self.ui.labelSets.setText(self.expr.solution[self.step]["s"])
        except RuntimeError as e:
            print(e)
        except IndexError:
            pass

        self.ui.tableWidget.removeCellWidget(0, 0)
        try:
            self.venn_diagram = None
        except AttributeError:
            pass
        if venn_num > 1:
            set_labels = []
            for s in self.expr.sets:
                set_labels.append(s)
            self.venn_diagram = VennDiagram(set_labels)
            try:
                self.venn_diagram.set(self.expr.solution[self.step]["v"])
                self.ui.tableWidget.setCellWidget(0, 0, self.venn_diagram)
            except IndexError:
                pass

    def pressNext(self):
        try:
            if self.step + 1 < len(self.expr.solution):
                self.step += 1
                self.ui.labelStep.setText("Step " + str(self.step + 1))
                self.ui.labelName.setText(self.expr.solution[self.step]["n"])
                self.ui.labelSets.setText(self.expr.solution[self.step]["s"])
                self.ui.labelResult.setText(self.expr.solution[self.step]["r"])
                try:
                    self.venn_diagram.set(self.expr.solution[self.step]["v"])
                except:
                    pass
        except IndexError:
            self.ui.labelStep.setText("Step " + str(0))

    def pressBack(self):
        try:
            if self.step > 0:
                self.step -= 1
                self.ui.labelStep.setText("Step " + str(self.step + 1))
                self.ui.labelName.setText(self.expr.solution[self.step]["n"])
                self.ui.labelSets.setText(self.expr.solution[self.step]["s"])
                self.ui.labelResult.setText(self.expr.solution[self.step]["r"])
                try:
                    self.venn_diagram.set(self.expr.solution[self.step]["v"])
                except:
                    pass
        except IndexError:
            self.ui.labelStep.setText("Step " + str(0))

    def center(self):
        qr = self.frameGeometry()
        cp = W.QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

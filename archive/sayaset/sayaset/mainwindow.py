import PyQt5.QtWidgets as W
import sayaset.uimainwindow as UMW
import random

__author__ = "IceArrow256"
__version__ = '1'


def set_to_str(s: set):
    if s:
        return str(s)[1:-1]
    else:
        return ""


def parse_set(str):
    return set(eval("{" + "{}".format(str) + "}"))


def cartesian(a: set, b: set):
    print("Cartesian", a, b)
    result = set()
    for i in a:
        for j in b:
            result.add((i, j))
    return result


def composition(p: set, q: set):
    print("Composition", p, q)
    error = False
    for i in p:
        if not ((type(i) is tuple) and len(i) == 2):
            error = True
    for i in q:
        if not ((type(i) is tuple) and len(i) == 2):
            error = True
    if not error:
        result = set()
        for i in p:
            for j in q:
                if i[1] == j[0]:
                    result.add((i[0], j[1]))
        return result
    else:
        return set()


def get_random_ratio(a: set, b: set):
    print("P", a, b)
    ratio = list(cartesian(a, b))
    result = set()
    if len(ratio) > 0:
        for i in range(random.randrange(len(ratio))):
            result.add(random.choice(ratio))
    return result


def get_projection(s: set):
    print("Projection", s)
    projections = {"pr1": set(), "pr2": set(), "pr12": set()}
    for i in s:
        if type(i) is str or type(i) is int:
            projections["pr1"].add(i)
    for i in s:
        if type(i) is tuple:
            if len(i) >= 1:
                projections["pr1"].add(i[0])
            if len(i) >= 2:
                projections["pr2"].add(i[1])
                projections["pr12"].add((i[0], i[1]))
    return projections


def get_sub_sets(s: set):
    print("Sub Sets", s)
    lens = []
    i = 0
    while i < len(s):
        r = random.randrange(1, len(s))
        if r + i <= len(s):
            lens.append(r)
            i += r
    sets = {}
    temp = list(s)
    for i in range(len(lens)):
        sets[chr(i + 65)] = set()
        for j in range(lens[i]):
            sets[chr(i + 65)].add(temp.pop(random.randrange(len(temp))))
    return sets


def get_addition(a: set, b: set):
    print("Addition", a, b)
    la = list(a)
    lb = list(b)
    error = False
    temp = []
    for i in la:
        if not(type(i) is tuple):
            temp.append((i,))
        else:
            temp.append(i)
    la = temp
    temp = []
    for i in lb:
        if not(type(i) is tuple):
            temp.append((i,))
        else:
            temp.append(i)
    lb = temp
    for i in la:
        if not ((type(i) is tuple) and len(i)):
            error = True
    for i in lb:
        if not ((type(i) is tuple) and len(i)):
            error = True
    if not error:
        result = []
        first = []
        second = []
        index = 0
        while la:
            first.append(la.pop(0))
            result.append([])
            while first:
                for pair in first:
                    for item in pair:
                        i = 0
                        while i < len(lb):
                            if item in lb[i]:
                                second.append(lb.pop(i))
                                continue
                            else:
                                i += 1
                for pair in first:
                    result[index].append(pair)
                first.clear()
                for pair in second:
                    for item in pair:
                        i = 0
                        while i < len(la):
                            if item in la[i]:
                                first.append(la.pop(i))
                                continue
                            else:
                                i += 1
                for pair in second:
                    result[index].append(pair)
                second.clear()
            index += 1
        while lb:
            result.append(lb.pop())
    else:
        print("Invalid input")
    addition = set()
    for data in result:
        addition_pair = set()
        for pair in data:
            for item in pair:
                addition_pair.add(item)
        addition.add(tuple(addition_pair))
    return addition


class MainWindow(W.QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = UMW.Ui_MainWindow()
        self.ui.setupUi(self)
        self.center()

        self.ui.pushButtonSolveAll.clicked.connect(self.solve_all)

    def solve_all(self):
        ratio_a = ratio_b = composition_p = composition_q = projection_a = sub_setting_a = addition_a = addition_b = cartesian_a = cartesian_b = set()
        try:
            ratio_a = parse_set(self.ui.lineEditRatioA.text())
            ratio_b = parse_set(self.ui.lineEditRatioB.text())
            composition_p = parse_set(self.ui.lineEditCompositionP.text())
            composition_q = parse_set(self.ui.lineEditCompositionQ.text())
            projection_a = parse_set(self.ui.lineEditProjectionA.text())
            sub_setting_a = parse_set(self.ui.lineEditSubSettingA.text())
            addition_a = parse_set(self.ui.lineEditAdditionA.text())
            addition_b = parse_set(self.ui.lineEditAdditionB.text())
            cartesian_a = parse_set(self.ui.lineEditCartesianA.text())
            cartesian_b = parse_set(self.ui.lineEditCartesianB.text())
        except SyntaxError:
            print("Invalid input data")
        except NameError:
            print("Invalid input data")

        self.ui.lineEditRatioAB.setText(set_to_str(cartesian(ratio_a, ratio_b)))
        self.ui.lineEditRatioBA.setText(set_to_str(cartesian(ratio_b, ratio_a)))
        self.ui.lineEditRatioAA.setText(set_to_str(cartesian(ratio_a, ratio_a)))
        self.ui.lineEditRatioBB.setText(set_to_str(cartesian(ratio_b, ratio_b)))
        self.ui.lineEditRatioP.setText(set_to_str(get_random_ratio(ratio_a, ratio_b)))

        self.ui.lineEditComposition.setText(set_to_str(composition(composition_p, composition_q)))

        projection = get_projection(projection_a)

        self.ui.lineEditPr1.setText(set_to_str(projection["pr1"]))
        self.ui.lineEditPr2.setText(set_to_str(projection["pr2"]))
        self.ui.lineEditPr12.setText(set_to_str(projection["pr12"]))

        self.ui.labelSubSets.setText(str(get_sub_sets(sub_setting_a))[1:-1])

        self.ui.lineEditAddition.setText(set_to_str(get_addition(addition_a, addition_b)))

        self.ui.lineEditCartesian.setText(set_to_str(cartesian(cartesian_a, cartesian_b)))
        print("----------------------------------------------------------------------")

    def center(self):
        qr = self.frameGeometry()
        cp = W.QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

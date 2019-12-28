import PyQt5.QtCore as C
import PyQt5.QtWidgets as W


class Matches(W.QTabWidget):
    def __init__(self, parent, data):
        super().__init__(parent)

        table = W.QTableView()
        matches_table = MatchesTable(self, data)
        proxyModel = C.QSortFilterProxyModel()
        proxyModel.setSourceModel(matches_table)
        proxyModel.setFilterKeyColumn(2)

        table.setModel(proxyModel)
        table.setSortingEnabled(True)
        # table.horizontalHeader().setSectionResizeMode(W.QHeaderView.Stretch)
        table.resizeColumnsToContents()
        table.setEditTriggers(W.QAbstractItemView.NoEditTriggers)
        # Создания сеточного макета, для текущего виджета
        layout = W.QGridLayout(self)
        layout.addWidget(table, 0, 0, 1, 1)


class MatchesTable(C.QAbstractTableModel):
    def __init__(self, parent, data):
        C.QAbstractTableModel.__init__(self, parent)
        self.matches = data
        self.colLabels = list(self.matches[0].keys())
        self.cached = []
        for match in self.matches:
            self.cached.append(list(match.values()))

    def rowCount(self, parent):
        return len(self.cached)

    def columnCount(self, parent):
        return len(self.colLabels)

    def data(self, index, role):
        if not index.isValid():
            return C.QVariant()
        elif role != C.Qt.DisplayRole and role != C.Qt.EditRole:
            return C.QVariant()
        value = ''
        if role == C.Qt.DisplayRole:
            row = index.row()
            col = index.column()
            value = self.cached[row][col]
        return C.QVariant(value)

    def headerData(self, section, orientation, role):
        if orientation == C.Qt.Horizontal and role == C.Qt.DisplayRole:
            return C.QVariant(self.colLabels[section])
        # заголовки строк
        if orientation == C.Qt.Vertical and role == C.Qt.DisplayRole:
            return C.QVariant("%s" % str(section + 1))
        return C.QVariant()

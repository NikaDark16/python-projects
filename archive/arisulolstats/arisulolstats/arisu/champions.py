import PyQt5.QtCore as C
import PyQt5.QtWidgets as W


class Champions(W.QTabWidget):
    def __init__(self, parent, data):
        super().__init__(parent)
        tab_champions_seasons = []
        for season in data:
            tab_champions_seasons.append(TabChampionsSeasons(self, data[season]))
            self.addTab(tab_champions_seasons[len(tab_champions_seasons) - 1], str(season))


class TabChampionsSeasons(W.QTabWidget):
    def __init__(self, parent, data):
        super().__init__(parent)

        table = W.QTableView()
        champions_table = ChampionsTable(self, data)
        proxyModel = C.QSortFilterProxyModel()
        proxyModel.setSourceModel(champions_table)
        proxyModel.setFilterKeyColumn(2)

        table.setModel(proxyModel)
        table.setSortingEnabled(True)
        # table.horizontalHeader().setSectionResizeMode(W.QHeaderView.Stretch)
        table.resizeColumnsToContents()

        # Создания сеточного макета, для текущего виджета
        layout = W.QGridLayout(self)
        layout.addWidget(table, 0, 0, 1, 1)


class ChampionsTable(C.QAbstractTableModel):
    def __init__(self, parent, data):
        C.QAbstractTableModel.__init__(self, parent)
        self.champions = data
        self.colLabels = list(self.champions[0].keys())
        self.cached = []
        for champion in self.champions:
            self.cached.append(list(champion.values()))

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

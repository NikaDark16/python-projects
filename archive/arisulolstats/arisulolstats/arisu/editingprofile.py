import PyQt5.QtWidgets as W

import arisulolstats.constants as constants


class EditingProfile(W.QDialog):
    def __init__(self, parent, name="", profile=[]):
        super(EditingProfile, self).__init__(parent)

        self.layout = W.QGridLayout(self)

        self.summoners = profile
        self.name = name

        self.label_profile_name = W.QLabel("Profile name", self)
        self.line_edit_profile_name = W.QLineEdit(self)
        self.summoners_table = SummonersTable(self, self.summoners)
        self.label_server = W.QLabel("Server", self)
        self.combo_box_server = W.QComboBox(self)
        self.label_summoner_name = W.QLabel("Summoner name", self)
        self.line_edit_summoner_name = W.QLineEdit(self)
        self.button_add = W.QPushButton("Add", self)
        self.button_delete = W.QPushButton("Delete", self)
        self.button_ok = W.QPushButton("OK", self)

        self.init()

        self.init_layout()

        self.init_connect()

    def init(self):
        if self.name != "":
            self.line_edit_profile_name.setText(self.name)
        self.combo_box_server.addItems(constants.REGIONAL_ENDPOINTS.keys())
        if self.summoners:
            self.setWindowTitle('Editing profiles')
        else:
            self.setWindowTitle('Adding profiles')

    def init_layout(self):
        self.layout.addWidget(self.label_profile_name, 0, 0)
        self.layout.addWidget(self.line_edit_profile_name, 0, 1, 1, 1)
        self.layout.addWidget(self.summoners_table, 1, 0, 1, 2)
        self.layout.addWidget(self.label_server, 2, 0, 1, 1)
        self.layout.addWidget(self.combo_box_server, 2, 1, 1, 1)
        self.layout.addWidget(self.label_summoner_name, 3, 0, 1, 1)
        self.layout.addWidget(self.line_edit_summoner_name, 3, 1, 1, 1)
        self.layout.addWidget(self.button_add, 4, 0, 1, 1)
        self.layout.addWidget(self.button_delete, 4, 1, 1, 1)
        self.layout.addWidget(self.button_ok, 5, 0, 1, 2)

    def init_connect(self):
        self.button_ok.clicked.connect(self.accept)
        self.button_add.clicked.connect(self.button_press_add)
        self.button_delete.clicked.connect(self.button_press_delete)

    def button_press_add(self):
        server = self.combo_box_server.currentText()
        summoner_name = self.line_edit_summoner_name.text()
        summoner = {"server": server, "name": summoner_name}
        if summoner_name != "" and summoner not in self.summoners:
            self.summoners.append(summoner)
            self.summoners_table.update_summoner(self.summoners)
            self.line_edit_summoner_name.setText("")

    def button_press_delete(self):
        summoner = self.summoners_table.delete(self.summoners)
        if summoner in self.summoners:
            self.summoners.remove(summoner)
        self.summoners_table.update_summoner(self.summoners)


class SummonersTable(W.QTableWidget):
    def __init__(self, parent, summoners=[]):
        super(SummonersTable, self).__init__(parent)

        self.init()

        self.update_summoner(summoners)

    def init(self):
        self.setColumnCount(2)
        self.setHorizontalHeaderLabels(["Server", "Summoner"])
        self.setEditTriggers(W.QAbstractItemView.NoEditTriggers)
        self.verticalHeader().hide()
        self.setSelectionBehavior(W.QAbstractItemView.SelectRows)

    def update_summoner(self, summoners):
        self.setRowCount(len(summoners))
        for i in range(len(summoners)):
            self.setItem(i, 0, W.QTableWidgetItem(summoners[i]["server"]))
            self.setItem(i, 1, W.QTableWidgetItem(summoners[i]["name"]))
        self.resizeColumnsToContents()

    def delete(self, summoners):
        current_row = self.currentRow()
        if current_row == -1:
            print("Is empty")
            return
        server = self.takeItem(current_row, 0).text()
        name = self.takeItem(current_row, 1).text()
        return {"server": server, "name": name}

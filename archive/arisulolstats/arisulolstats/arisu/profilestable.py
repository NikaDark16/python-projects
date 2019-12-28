import PyQt5.QtWidgets as W


class ProfilesTable(W.QTableWidget):
    def __init__(self, parent, profiles=[]):
        super(ProfilesTable, self).__init__(parent)

        self.init()

        self.update_profiles(profiles)

    def init(self):
        self.setColumnCount(2)
        self.setHorizontalHeaderLabels(["Name", "Number of summoners"])
        self.setEditTriggers(W.QAbstractItemView.NoEditTriggers)
        self.verticalHeader().hide()
        self.setSelectionBehavior(W.QAbstractItemView.SelectRows)

    def update_profiles(self, profiles):
        self.setRowCount(len(profiles))
        i = 0
        for profile in profiles:
            self.setItem(i, 0, W.QTableWidgetItem(profile))
            self.setItem(i, 1, W.QTableWidgetItem(str(len(profiles[profile]))))
            i += 1
        self.resizeColumnsToContents()

    def get_current_profile_name(self):
        current_row = self.currentRow()
        if current_row == -1:
            print("Is empty")
            return
        profile = self.item(current_row, 0).text()
        return profile

    def delete(self, profiles):
        current_row = self.currentRow()
        if current_row == -1:
            print("Is empty")
            return
        profile = self.takeItem(current_row, 0).text()
        if profile in profiles:
            return profile

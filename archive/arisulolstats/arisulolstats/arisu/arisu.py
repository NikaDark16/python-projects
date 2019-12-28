__author__ = 'IceArrow256'
import os
import sys

import PyQt5.QtWidgets as W
import ia256utilities.filesystem as fs

import arisulolstats.arisu.console as console
import arisulolstats.arisu.editingprofile as editingprofile
import arisulolstats.arisu.profilestable as profilestable
import arisulolstats.arisu.profilestabs as profilestabs
import arisulolstats.lolstats.lolstats as lolstats


class Arisu(W.QMainWindow):
    def __init__(self):
        super().__init__()


        self.widget = W.QWidget(self)
        self.layout = W.QGridLayout(self.widget)

        self.profiles = fs.load_json("./data/profiles.json")
        self.api_key_file = fs.load_json("./data/api.json")

        self.button_update = W.QPushButton("Update", self.widget)
        self.button_add = W.QPushButton("Add", self.widget)
        self.button_delete = W.QPushButton("Delete", self.widget)
        self.button_edit = W.QPushButton("Edit", self.widget)
        self.button_clear = W.QPushButton("Clear", self.widget)
        self.line_edit_api_key = W.QLineEdit(self.widget)
        self.console = console.Console(self.widget)
        self.profiles_table = profilestable.ProfilesTable(self.widget)
        self.profiles_tabs = profilestabs.ProfilesTabs(self.widget)

        self.lol_stats = lolstats.LoLStats(self.console, self.button_update)

        self.init_ui()

        self.init_layout()

        self.init_connect()

    def __del__(self):
        fs.save_json(self.profiles, "./data/profiles.json")
        self.api_key_file["apiKey"] = self.line_edit_api_key.text()
        if len(self.api_key_file["apiKey"]) == 42 and self.api_key_file["apiKey"][:6] == 'RGAPI-':
            fs.save_json(self.api_key_file, "./data/api.json")

    def init_ui(self):
        self.profiles_table.update_profiles(self.profiles)
        if "apiKey" in self.api_key_file:
            self.line_edit_api_key.setText(self.api_key_file["apiKey"])
        self.resize(1280, 720)
        self.center()
        self.setWindowTitle('Arisu')
        self.setCentralWidget(self.widget)
        self.show()

    def init_layout(self):
        self.layout.addWidget(self.console, 0, 0, 2, 1)
        self.layout.addWidget(self.button_clear, 2, 0, 1, 1)
        self.layout.addWidget(self.profiles_tabs, 0, 1, 1, 1)
        self.layout.addWidget(self.profiles_table, 0, 2, 1, 2)
        self.layout.addWidget(self.line_edit_api_key, 1, 1, 1, 1)
        self.layout.addWidget(self.button_update, 2, 1, 1, 1)
        self.layout.addWidget(self.button_add, 1, 2, 1, 1)
        self.layout.addWidget(self.button_delete, 1, 3, 1, 1)
        self.layout.addWidget(self.button_edit, 2, 2, 1, 2)

    def init_connect(self):
        self.button_update.clicked.connect(self.press_button_update)
        self.button_add.clicked.connect(self.press_button_add)
        self.button_delete.clicked.connect(self.press_button_delete)
        self.button_edit.clicked.connect(self.press_button_edit)
        self.button_clear.clicked.connect(self.console.clear)

    def center(self):
        qr = self.frameGeometry()
        cp = W.QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def press_button_update(self):
        self.api_key_file["apiKey"] = self.line_edit_api_key.text()
        if len(self.api_key_file["apiKey"]) == 42 and self.api_key_file["apiKey"][:6] == 'RGAPI-':
            fs.save_json(self.api_key_file, "./data/api.json")
            self.lol_stats.set_api_key_and_profiles(self.api_key_file["apiKey"], self.profiles)
            self.lol_stats.start()
        else:
            self.console.write_line("Invalid RGAPI key. Example RGAPI-XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")

    def press_button_add(self):
        editing_profile = editingprofile.EditingProfile(self, "", [])
        if editing_profile.exec_() == W.QDialog.Accepted:
            name = editing_profile.line_edit_profile_name.text()
            if name != "":
                self.profiles[name] = editing_profile.summoners
                self.profiles_table.update_profiles(self.profiles)
                fs.save_json(self.profiles, "./data/profiles.json")
        editing_profile.deleteLater()

    def press_button_delete(self):
        profile = self.profiles_table.delete(self.profiles)
        if profile:
            del self.profiles[profile]
            self.profiles_table.update_profiles(self.profiles)
            fs.save_json(self.profiles, "./data/profiles.json")

    def press_button_edit(self):
        old_name = self.profiles_table.get_current_profile_name()
        if old_name:
            editing_profile = editingprofile.EditingProfile(self, old_name, self.profiles[old_name])
            if editing_profile.exec_() == W.QDialog.Accepted:
                name = editing_profile.line_edit_profile_name.text()
                if name != "":
                    if old_name != name:
                        del self.profiles[old_name]
                    self.profiles[name] = editing_profile.summoners
                    self.profiles_table.update_profiles(self.profiles)
                    fs.save_json(self.profiles, "./data/profiles.json")
            editing_profile.deleteLater()


def main():
    app = W.QApplication(sys.argv)
    window = Arisu()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()

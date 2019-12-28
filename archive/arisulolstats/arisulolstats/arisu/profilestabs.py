import glob
import os

import PyQt5.QtWidgets as W
import ia256utilities.filesystem as fs

import arisulolstats.arisu.tabprofile as tabprofile


class ProfilesTabs(W.QTabWidget):
    def __init__(self, parent):
        super(ProfilesTabs, self).__init__(parent)
        profiles = {}
        profiles_tab = []

        for file in glob.glob("./data/data/*.json"):
            profile = os.path.splitext(os.path.basename(file))[0]
            profiles[profile] = fs.load_json(file)

        for profile in profiles.keys():
            profiles_tab.append(tabprofile.TabProfile(self, profiles[profile]))
            self.addTab(profiles_tab[len(profiles_tab) - 1], profile)

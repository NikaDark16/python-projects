import PyQt5.QtWidgets as Widgets

import arisulolstats.arisu.champions as champions
import arisulolstats.arisu.matches as matches
import arisulolstats.arisu.summoner as summoner


class TabProfile(Widgets.QTabWidget):
    def __init__(self, parent, data):
        super().__init__(parent)
        self.addTab(summoner.Summoner(self, data["summonerTab"]), "Summoner")
        self.addTab(champions.Champions(self, data["championsTab"]), "Champions")
        self.addTab(matches.Matches(self, data["matchesTab"]), "Matches")

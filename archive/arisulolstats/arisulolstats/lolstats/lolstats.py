import PyQt5.QtCore as C

import arisulolstats.lolstats.championmastery as championmasteries
import arisulolstats.lolstats.data as data
import arisulolstats.lolstats.database as database
import arisulolstats.lolstats.league as league
import arisulolstats.lolstats.matches as matches
import arisulolstats.lolstats.matchlist as matchlist
import arisulolstats.lolstats.preprocessed as preprocessed
import arisulolstats.lolstats.processing as processing
import arisulolstats.lolstats.riotgamesapi as riotgamesapi
import arisulolstats.lolstats.summoner as summoner


class LoLStats(C.QThread):

    def __init__(self, console, update_button):
        """

        :type update_button: PyQt5.QtWidgets.QPushButton.QPushButton
        :type console: darkarisulolstats.arisu.console.Console
        """
        super(LoLStats, self).__init__()
        self.console = console
        self.update_button = update_button
        self.api_key = ""
        self.profiles = {}
        self.summoners = []

    def set_api_key_and_profiles(self, api_key, profiles):
        self.api_key = api_key
        self.profiles = profiles
        for profile in self.profiles:
            for summoner in self.profiles[profile]:
                if summoner not in self.summoners:
                    self.summoners.append(summoner)

    def check_start(self):
        if self.api_key != "" and self.summoners:
            return True
        else:
            self.console.write_line("No summoner specified")
            return False

    def run(self):
        if self.check_start():
            self.update_button.setDisabled(True)
            rga = riotgamesapi.RiotGamesApi(self.api_key)
            db = database.Database()
            self.console.write_line("Start LoLStats")
            for self.summoner in self.summoners:
                summoner.Summoner(self.console, db, rga, self.summoner)
                league.League(self.console, db, rga, self.summoner)
                championmasteries.ChampionMastery(self.console, db, rga, self.summoner)
                matchlist.Matchlist(self.console, db, rga, self.summoner)
                matches.Matches(self.console, db, rga, self.summoner)
                data.Data(self.console, db, rga, self.summoner)
            for profile in self.profiles:
                preprocessed.Preprocessed(self.console, db, profile, self.profiles[profile])
                processing.Processing(db, profile, self.profiles[profile])
            self.console.write_line("End LoLStats")
            self.update_button.setDisabled(False)

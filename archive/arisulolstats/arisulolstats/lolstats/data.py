import os
import time

import ia256utilities.filesystem as fs
import requests

import arisulolstats.constants as constants


class Data:
    def __init__(self, c, db, rga, s):
        """
        :type db: arisulolstats.lolstats.Database
        :type s: dict
        :type rga: darkarisulolstats.lolstats.riotgamesapi.RiotGamesApi
        :type c: darkarisulolstats.arisu.console.Console
        """
        work = 2
        while work != 0:
            try:
                c.write_line("Data lolstats({}): {}".format(s["server"], s["name"]))
                version = self.get_version()
                self.profile_icon(db, s, version)
                self.champions(db, rga, version)
                self.leagues(db, s)
                work = 0
            except requests.exceptions.HTTPError:
                if work != 1:
                    c.write_line("Data lolstats({}) error: {}. Try to wait 1 minutes".format(s["server"], s["name"]))
                    work -= 1
                    time.sleep(60)
                else:
                    work = 0
            except KeyError:
                c.write_line("Data lolstats({}) error while parsing: {}".format(s["server"], s["name"]))
                work = 0

    @staticmethod
    def profile_icon(db, s, version):
        """
        :type db: arisulolstats.lolstats.Database
        :type s: dict
        :param version: str
        """
        profile_icon_id = db.summoners.get(s)["profileIconId"]
        if not DataDragon.check_profile_icon(profile_icon_id):
            DataDragon.add_profile_icon(profile_icon_id, requests.get(
                "http://ddragon.leagueoflegends.com/cdn/{}/img/profileicon/{}.png".format(version,
                                                                                          profile_icon_id)).content)

    @staticmethod
    def champions(db, rga, version):
        """
        :param version: str
        :type db: arisulolstats.lolstats.Database
        :type rga: darkarisulolstats.lolstats.riotgamesapi.RiotGamesApi
        """
        champions = rga.data_dragon.champions(version)["data"]
        db.data.add("champions", champions)
        for champion in champions.keys():
            if not DataDragon.check_champion_icon(champion):
                DataDragon.add_champion_icon(champion, requests.get(
                    "http://ddragon.leagueoflegends.com/cdn/{}/img/champion/{}.png".format(version, champion)).content)

    @staticmethod
    def leagues(db, s):
        """
        :type db: arisulolstats.lolstats.Database
        :type s: dict
        """
        leagues = db.leagues.get(s)
        if leagues:
            for league in leagues:
                tier = league["tier"].lower()
                rank = constants.RANK[league["rank"]]
                if not DataDragon.check_league_icon(tier, rank):
                    DataDragon.add_league_icon(tier, rank, requests.get(
                        "https://opgg-static.akamaized.net/images/medals/{}_{}.png".format(tier, rank)).content)

    @staticmethod
    def get_version():
        return requests.get("https://ddragon.leagueoflegends.com/realms/na.json").json()["v"]


class DataDragon:
    @staticmethod
    def add_profile_icon(profile_icon_id, data):
        fs.save_binary(data, "./data/profileicons/{}.png".format(profile_icon_id))

    @staticmethod
    def add_champion_icon(champion_key, data):
        fs.save_binary(data, "./data/champions/{}.png".format(champion_key))

    @staticmethod
    def add_league_icon(tier, rank, data):
        fs.save_binary(data, "./data/leagues/{}_{}.png".format(tier, rank))

    @staticmethod
    def get_profile_icon_path(profile_icon_id):
        if DataDragon.check_profile_icon(profile_icon_id):
            return "./data/profileicons/{}.png".format(profile_icon_id)
        else:
            return ""

    @staticmethod
    def get_league_icon_path(tier, rank):
        tier = tier.lower()
        rank = int(rank)
        if DataDragon.check_league_icon(tier, rank):
            return "./data/leagues/{}_{}.png".format(tier, rank)
        else:
            return ""

    @staticmethod
    def get_champion_icon_path(db, name):
        champions = db.data.get("champions")
        for champion in champions:
            if champions[champion]["name"] == name:
                champion_key = champion
                break
        if DataDragon.check_champion_icon(champion_key):
            return "./data/champions/{}.png".format(champion_key)
        else:
            return ""

    @staticmethod
    def check_league_icon(tier, rank):
        return os.path.isfile("./data/leagues/{}_{}.png".format(tier, rank))

    @staticmethod
    def check_profile_icon(profile_icon_id):
        return os.path.isfile("./data/profileicons/{}.png".format(profile_icon_id))

    @staticmethod
    def check_champion_icon(champion_key):
        return os.path.isfile("./data/champions/{}.png".format(champion_key))

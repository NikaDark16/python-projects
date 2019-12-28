class Summoner:
    def __init__(self, c, db, rga, s):
        """
        :type db: darkarisulolstats.lolstats.database.Database
        :type s: dict
        :type rga: darkarisulolstats.lolstats.riotgamesapi.RiotGamesApi
        :type c: darkarisulolstats.arisu.console.Console
        """
        db.summoners.add(s, rga.summoner_by_name(s))
        c.write_line("Summoner by name - {} from {}".format(s["name"], s["server"]))

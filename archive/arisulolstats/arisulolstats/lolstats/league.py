class League:
    def __init__(self, c, db, rga, s):
        """
        :type db: darkarisulolstats.lolstats.database.Database
        :type s: dict
        :type rga: darkarisulolstats.lolstats.riotgamesapi.RiotGamesApi
        :type c: darkarisulolstats.arisu.console.Console
        """
        summoner = db.summoners.get(s)
        if summoner["summonerLevel"] >= 30:
            c.write_line("League by summoner - {} from {}".format(s["name"], s["server"]))
            db.leagues.add(s, rga.league_by_summoner(s, summoner))

class ChampionMastery:
    def __init__(self, c, db, rga, s):
        """
        :type db: darkarisulolstats.lolstats.database.Database
        :type s: dict
        :type rga: darkarisulolstats.lolstats.riotgamesapi.RiotGamesApi
        :type c: darkarisulolstats.arisu.console.Console
        """
        summoner = db.summoners.get(s)
        c.write_line("Champion mastery by summoner - {} from {}".format(s["name"], s["server"]))
        db.champion_masteries.add(s, rga.champion_mastery_by_summoner(s, summoner))

import requests.exceptions as exceptions

import arisulolstats.constants as constants


class Matchlist:
    def __init__(self, c, db, rga, s):
        """
        :type db: darkarisulolstats.lolstats.database.Database
        :type s: dict
        :type rga: darkarisulolstats.lolstats.riotgamesapi.RiotGamesApi
        :type c: darkarisulolstats.arisu.console.Console
        """
        inv_regional_endpoint = {v: k for k, v in constants.REGIONAL_ENDPOINTS.items()}
        while True:
            try:
                summoner = db.summoners.get(s)
                full_matchlist = db.matchlists.get(s)
                need_games = 0
                for match in rga.match_matchlist_by_account(s, summoner)["matches"]:
                    exist = False
                    for old_match in full_matchlist:
                        if match["gameId"] == old_match["gameId"]:
                            exist = True
                            break
                    if not exist:
                        need_games += 1
                if need_games == 100:
                    need_games = rga.match_matchlist_by_account(s, summoner, begin_index=1000)["totalGames"]
                c.write_line(
                    "Matchlist by account - {} from {}. Need games: {}".format(s["name"], s["server"], need_games))
                index = 0
                while index < need_games:
                    matchlist = rga.match_matchlist_by_account(s, summoner, begin_index=index)
                    c.write_line("Matchlist by account - {} from {}. Index = {}".format(s["name"], s["server"], index))
                    for match in matchlist["matches"]:
                        exist = False
                        for old_match in full_matchlist:
                            if match["gameId"] == old_match["gameId"]:
                                old_match = match
                                exist = True
                                break
                        if not exist:
                            match["platformId"] = inv_regional_endpoint[match["platformId"]]
                            full_matchlist.append(match)
                    index += 100
                full_matchlist = sorted(full_matchlist, key=lambda i: i['timestamp'], reverse=True)
                db.matchlists.add(s, full_matchlist)
                break
            except exceptions.HTTPError as e:
                status_code = e.response.status_code
                if status_code == 404:
                    c.write_line("Matchlist by account - {} from {}. Error".format(s["name"], s["server"]))
                    break
                else:
                    c.write_line(str(status_code))
                    break

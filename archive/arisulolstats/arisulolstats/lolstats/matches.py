import requests.exceptions as exceptions

import arisulolstats.constants as constants


class Matches:
    def __init__(self, c, db, rga, s):
        """
        :type db: darkarisulolstats.lolstats.database.Database
        :type s: dict
        :type rga: darkarisulolstats.lolstats.riotgamesapi.RiotGamesApi
        :type c: darkarisulolstats.arisu.console.Console
        """
        inv_regional_endpoint = {v: k for k, v in constants.REGIONAL_ENDPOINTS.items()}
        c.write_line("Matches by ids - {} from {}".format(s["name"], s["server"]))
        matchlist = db.matchlists.get(s)
        for match in matchlist:
            game_id = match["gameId"]
            server = match["platformId"]
            if not db.matches.check(server, game_id):
                while True:
                    try:
                        game = rga.match_by_id(server, game_id)
                        c.write_line("Match {} from {}".format(game_id, server))
                        game["platformId"] = inv_regional_endpoint[game["platformId"]]
                        db.matches.add(server, game_id, game)
                        break
                    except exceptions.HTTPError as e:
                        status_code = e.response.status_code
                        if status_code == 404:
                            c.write_line("Matchlist by name - {} from {}. Error".format(s["name"], server))
                            break
                        else:
                            c.write_line(str(status_code))
                            break

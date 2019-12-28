import time


class Preprocessed:
    def __init__(self, c, db, profile, summoners):
        """
        :type profile: str
        :type db: darkarisulolstats.lolstats.database.Database
        :type c: darkarisulolstats.arisu.console.Console
        """
        db.preprocessed.add(profile, "matchlists", generate_matchlist(c, db, summoners))
        db.preprocessed.add(profile, "champions", generate_champions(db, profile, summoners))
        db.preprocessed.add(profile, "roles", generate_role(db, profile))


def generate_matchlist(c, db, ss):
    """
    :type c: darkarisulolstats.arisu.console.Console
    """
    matchlist = []
    summoners = []
    for s in ss:
        summoner = {}
        summoner["data"] = db.summoners.get(s)
        summoner["name"] = summoner["data"]["name"]
        summoner["summoner"] = s
        summoners.append(summoner)
    champions_list = db.data.get("champions")
    for summoner in summoners:
        old_matchlist = db.matchlists.get(summoner["summoner"])
        for old_match in old_matchlist:
            match = {}
            game = db.matches.get(old_match["platformId"], old_match["gameId"])
            if game:
                for participant in game["participantIdentities"]:
                    if participant["player"]["summonerName"] == summoner["name"]:
                        participant_id = participant["participantId"]
                        break
                for participant in game["participants"]:
                    if participant["participantId"] == participant_id:
                        match["server"] = old_match["platformId"]
                        match["season"] = get_season(old_match["season"])
                        match["name"] = summoner["name"]
                        match["champion"] = get_champion_name(champions_list, old_match["champion"])
                        try:
                            match["role"] = get_role(match["champion"], old_match["role"], old_match["lane"])
                        except KeyError:
                            match["role"] = "None"
                        match["win"] = participant["stats"]["win"]
                        match["queue"] = get_queue_name(game["queueId"])
                        match["kills"] = participant["stats"]["kills"]
                        match["deaths"] = participant["stats"]["deaths"]
                        match["assists"] = participant["stats"]["assists"]
                        if match["deaths"] == 0:
                            match["deaths"] = 1
                        match["kda"] = (match["kills"] + match["assists"]) / match["deaths"]
                        if "neutralMinionsKilledTeamJungle" not in participant["stats"]:
                            participant["stats"]["neutralMinionsKilledTeamJungle"] = 0
                        if "neutralMinionsKilledEnemyJungle" not in participant["stats"]:
                            participant["stats"]["neutralMinionsKilledEnemyJungle"] = 0
                        match["cs"] = participant["stats"]["totalMinionsKilled"] + participant["stats"][
                            "neutralMinionsKilled"] + participant["stats"]["neutralMinionsKilledTeamJungle"] + \
                                      participant["stats"]["neutralMinionsKilledEnemyJungle"]
                        match["csPerMin"] = match["cs"] / (game["gameDuration"] / 60)
                        match["date"] = get_time_to_string(game["gameCreation"])
                        match["duration"] = game["gameDuration"] / 60
                        match["damage"] = participant["stats"]["totalDamageDealtToChampions"]
                        break
                if match["queue"] != "Trash" and match["duration"] > 5:
                    matchlist.append(match)
    return matchlist


def generate_champions(db, name, ss):
    champions = {"all": {}}
    champions_list = db.data.get("champions")
    matchlist = db.preprocessed.get(name, "matchlists")
    champion_mastery = {}
    for s in ss:
        raw_champion_mastery = db.champion_masteries.get(s)
        for champion in raw_champion_mastery:
            champion_name = get_champion_name(champions_list, champion["championId"])
            if champion_name not in champion_mastery:
                champion_mastery[champion_name] = {}
                champion_mastery[champion_name]["points"] = champion['championPoints']
            else:
                champion_mastery[champion_name]["points"] += champion['championPoints']

    for match in matchlist:
        if match["season"] not in champions:
            champions[match["season"]] = {}
        if match["champion"] not in champions[match["season"]]:
            champions[match["season"]][match["champion"]] = {}
        if match["champion"] not in champions["all"]:
            champions["all"][match["champion"]] = {}
    for champion in champion_mastery:
        if champion not in champions["all"]:
            champions["all"][champion] = {}
    for season in champions:
        for champion in champions[season]:
            champions[season][champion]["wins"] = 0
            champions[season][champion]["losses"] = 0
            champions[season][champion]["games"] = 0
            champions[season][champion]["winRatio"] = 0
            champions[season][champion]["kills"] = 0
            champions[season][champion]["killsAll"] = 0
            champions[season][champion]["deaths"] = 0
            champions[season][champion]["deathsAll"] = 0
            champions[season][champion]["assists"] = 0
            champions[season][champion]["assistsAll"] = 0
            champions[season][champion]["kda"] = 0
            champions[season][champion]["damage"] = 0
            champions[season][champion]["damageAll"] = 0
            champions[season][champion]["cs"] = 0
            champions[season][champion]["csAll"] = 0
            champions[season][champion]["csPerMin"] = 0
            champions[season][champion]["duration"] = 0
            champions[season][champion]["durationAll"] = 0
            try:
                champions[season][champion]["lastPlayTime"] = champion_mastery[champion]["lastPlayTime"]
            except:
                champions[season][champion]["lastPlayTime"] = 0
            try:
                champions[season][champion]["level"] = champion_mastery[champion]["level"]
            except:
                champions[season][champion]["level"] = 0
            try:
                champions[season][champion]["points"] = champion_mastery[champion]["points"]
            except:
                champions[season][champion]["points"] = 0
            try:
                champions[season][champion]["pointsSinceLastLevel"] = champion_mastery[champion]["pointsSinceLastLevel"]
                champions[season][champion]["pointsUntilNextLevel"] = champion_mastery[champion]["pointsUntilNextLevel"]
            except:
                champions[season][champion]["pointsSinceLastLevel"] = 0
                champions[season][champion]["pointsUntilNextLevel"] = 0
    for match in matchlist:
        if match["win"]:
            champions[match["season"]][match["champion"]]["wins"] += 1
            champions["all"][match["champion"]]["wins"] += 1
        else:
            champions[match["season"]][match["champion"]]["losses"] += 1
            champions["all"][match["champion"]]["losses"] += 1
        champions[match["season"]][match["champion"]]["killsAll"] += match["kills"]
        champions["all"][match["champion"]]["killsAll"] += match["kills"]
        champions[match["season"]][match["champion"]]["deathsAll"] += match["deaths"]
        champions["all"][match["champion"]]["deathsAll"] += match["deaths"]
        champions[match["season"]][match["champion"]]["assistsAll"] += match["assists"]
        champions["all"][match["champion"]]["assistsAll"] += match["assists"]
        champions[match["season"]][match["champion"]]["damageAll"] += match["damage"]
        champions["all"][match["champion"]]["damageAll"] += match["damage"]
        champions[match["season"]][match["champion"]]["csAll"] += match["cs"]
        champions["all"][match["champion"]]["csAll"] += match["cs"]
        champions[match["season"]][match["champion"]]["durationAll"] += match["duration"]
        champions["all"][match["champion"]]["durationAll"] += match["duration"]
    for season in champions:
        for champion in champions[season]:
            champions[season][champion]["games"] = champions[season][champion]["wins"] + champions[season][champion][
                "losses"]
            if champions[season][champion]["games"] != 0:
                champions[season][champion]["winRatio"] = champions[season][champion]["wins"] / \
                                                          champions[season][champion]["games"]
                champions[season][champion]["kills"] = champions[season][champion]["killsAll"] / \
                                                       champions[season][champion]["games"]
                champions[season][champion]["deaths"] = champions[season][champion]["deathsAll"] / \
                                                        champions[season][champion]["games"]
                champions[season][champion]["assists"] = champions[season][champion]["assistsAll"] / \
                                                         champions[season][champion]["games"]
                champions[season][champion]["kda"] = (champions[season][champion]["killsAll"] +
                                                      champions[season][champion]["assistsAll"]) / \
                                                     champions[season][champion]["deathsAll"]
                champions[season][champion]["damage"] = champions[season][champion]["damageAll"] / \
                                                        champions[season][champion]["games"]
                champions[season][champion]["cs"] = champions[season][champion]["csAll"] / \
                                                    champions[season][champion]["games"]
                champions[season][champion]["csPerMin"] = champions[season][champion]["csAll"] / \
                                                          champions[season][champion]["durationAll"]
                champions[season][champion]["duration"] = champions[season][champion]["durationAll"] / \
                                                          champions[season][champion]["games"]
    for season in champions:
        champions[season] = dict(sorted(champions[season].items(), key=lambda x: x[1]['games'], reverse=True))
    return champions


def generate_role(db, profile):
    matchlist = db.preprocessed.get(profile, "matchlists")
    roles = {"all": {}}
    roles["all"]["All"] = {}
    roles["all"]["All"]["wins"] = 0
    roles["all"]["All"]["losses"] = 0
    for match in matchlist:
        if match["season"] not in roles:
            roles[match["season"]] = {}
        if match["role"] not in roles[match["season"]]:
            roles[match["season"]][match["role"]] = {}
        if match["role"] not in roles["all"]:
            roles["all"][match["role"]] = {}
        roles["all"][match["role"]]["wins"] = 0
        roles["all"][match["role"]]["losses"] = 0
        roles[match["season"]]["All"] = {}
        roles[match["season"]]["All"]["wins"] = 0
        roles[match["season"]]["All"]["losses"] = 0
        roles[match["season"]][match["role"]]["wins"] = 0
        roles[match["season"]][match["role"]]["losses"] = 0
    for match in matchlist:
        if match["win"]:
            roles[match["season"]][match["role"]]["wins"] += 1
            roles[match["season"]]['All']["wins"] += 1
            roles['all']['All']["wins"] += 1
            roles["all"][match["role"]]["wins"] += 1
        else:
            roles[match["season"]][match["role"]]["losses"] += 1
            roles[match["season"]]['All']["losses"] += 1
            roles['all']['All']["losses"] += 1
            roles["all"][match["role"]]["losses"] += 1
    return roles


def get_champion_name(champions, champion_id):
    for champion in champions.keys():
        if int(champions[champion]["key"]) == champion_id:
            return champions[champion]["name"]


def get_role(name, role, lane):
    popular_adc = (
        "Ashe", "Caitlyn", "Corki", "Draven", "Ezreal", "Heimerdinger", "Jhin", "Jinx", "Kai'Sa", "Kalista", "Kog'Maw",
        "Lucian", "Miss Fortune", "Mordekaiser", "Neeko", "Quinn", "Sivir", "Taric", "Tristana", "Twitch", "Varus",
        "Vayne", "Xayah")
    popular_support = (
        "Alistar", "Annie", "Bard", "Blitzcrank", "Brand", "Braum", "Fiddlesticks", "Galio", "Gragas", "Illaoi",
        "Janna", "Karma", "Leona", "Lulu", "Lux", "Malphite", "Maokai", "Morgana", "Nami", "Nautilus", "Neeko", "Poppy",
        "Pyke", "Rakan", "Shen", "Sion", "Sona", "Soraka", "Tahm Kench", "Taliyah", "Taric", "Thresh", "Veigar",
        "Vel'Koz", "Volibear", "Xerath", "Zilean", "Zyra")
    if lane != "BOTTOM" and lane != "NONE":
        return lane.capitalize()
    elif role == 'DUO_CARRY':
        return "ADC"
    elif role == 'DUO_SUPPORT':
        return "Support"
    elif name in popular_adc:
        return "ADC"
    elif name in popular_support:
        return "Support"
    else:
        return "None"


def get_time_to_string(c_time):
    return str(time.strftime('%Y.%m.%d %H:%M', time.gmtime(c_time / 1000.)))


def get_season(season):
    return round((season + 5.5) / 2)


def get_queue_name(queue_id):
    if queue_id in (2, 14, 61, 400, 430):
        return "Normal"
    elif queue_id in (4, 6, 410, 420):
        return "Ranked Solo"
    elif queue_id in (42, 440):
        return "Ranked Flex"
    else:
        return "Trash"

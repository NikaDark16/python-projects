import ia256utilities.filesystem as fs

import arisulolstats.constants as constants
import arisulolstats.lolstats.data as data


class Processing:
    def __init__(self, db, profile, summoners):
        data = {}
        data["summonerTab"] = generate_summoner_tab(db, profile, summoners)
        data["matchesTab"] = generate_matches_tab(db, profile, summoners)
        data["championsTab"] = generate_champions_tab(db, profile, summoners)
        fs.save_json(data, "./data/data/{}.json".format(profile))


def generate_summoner_tab(db, profile, summoners):
    summoner_tab = {}
    summoner_tab["summoner"] = generate_summoner_tab_summoner(db, profile, summoners)
    summoner_tab["leagues"] = generate_summoner_tab_leagues(db, profile, summoners)
    summoner_tab["seasons"] = generate_summoner_tab_seasons(db, profile, summoners)
    return summoner_tab


def generate_summoner_tab_summoner(db, profile, ss):
    """
    :type db: darkarisulolstats.lolstats.database.Database
    """
    summoner = {}
    for s in ss:
        raw_summoner = db.summoners.get(s)
        if "profileIconPath" not in summoner:
            summoner["profileIconPath"] = data.DataDragon.get_profile_icon_path(raw_summoner["profileIconId"])
        summoner["name"] = profile
        if "level" not in summoner:
            summoner["level"] = raw_summoner["summonerLevel"]
        else:
            summoner["level"] += raw_summoner["summonerLevel"]

    summoner["Playtime"] = 0
    raw_matches = db.preprocessed.get(profile, "matchlists")
    for raw_match in raw_matches:
        summoner["Playtime"] += raw_match["duration"]
    return summoner


def generate_summoner_tab_leagues(db, profile, ss):
    """
    :type db: darkarisulolstats.lolstats.database.Database
    """
    leagues = {}
    for s in ss:
        raw_leagues = db.leagues.get(s)
        for raw_league in raw_leagues:
            if raw_league["queueType"] == "RANKED_SOLO_5x5":
                league_name = "Ranked Solo"
            elif raw_league["queueType"] == "RANKED_FLEX_SR":
                league_name = "Ranked Flex"
            if league_name not in leagues:
                leagues[league_name] = {}
            if "tier" not in leagues[league_name]:
                leagues[league_name]["tier"] = raw_league["tier"].capitalize()
            if "rank" not in leagues[league_name]:
                leagues[league_name]["rank"] = constants.RANK[raw_league["rank"]]
            if "leagueIconPath" not in leagues[league_name]:
                leagues[league_name]["leagueIconPath"] = data.DataDragon.get_league_icon_path(
                    leagues[league_name]["tier"],
                    leagues[league_name]["rank"])
            if "points" not in leagues[league_name]:
                leagues[league_name]["points"] = raw_league["leaguePoints"]
            if "wins" not in leagues[league_name]:
                leagues[league_name]["wins"] = raw_league["wins"]
            else:
                leagues[league_name]["wins"] += raw_league["wins"]
            if "losses" not in leagues[league_name]:
                leagues[league_name]["losses"] = raw_league["losses"]
            else:
                leagues[league_name]["losses"] += raw_league["losses"]

    return leagues


def generate_summoner_tab_seasons(db, profile, summoners):
    """
    :type db: darkarisulolstats.lolstats.database.Database
    """
    seasons = {}
    raw_roles = db.preprocessed.get(profile, "roles")
    raw_champions = db.preprocessed.get(profile, "champions")
    count = 0
    for season in raw_roles:
        seasons[season] = {}
        seasons[season]["All"] = {}
        seasons[season]["All"]["wins"] = raw_roles[season]["All"]["wins"]
        seasons[season]["All"]["losses"] = raw_roles[season]["All"]["losses"]
        seasons[season]["Roles"] = {}
        for role in raw_roles[season]:
            if role != "All":
                seasons[season]["Roles"][role] = {}
                seasons[season]["Roles"][role]["wins"] = raw_roles[season][role]["wins"]
                seasons[season]["Roles"][role]["losses"] = raw_roles[season][role]["losses"]
                seasons[season]["Roles"][role]["games"] = raw_roles[season][role]["wins"] + raw_roles[season][role][
                    "losses"]
                count += 1
        seasons[season]["Roles"] = dict(
            sorted(seasons[season]["Roles"].items(), key=lambda x: x[1]['games'], reverse=True))
        seasons[season]["Champions"] = {}
        count_champions = 0
        for champion in raw_champions[season]:
            seasons[season]["Champions"][champion] = {}
            seasons[season]["Champions"][champion]["iconPath"] = data.DataDragon.get_champion_icon_path(db,
                                                                                                        champion)
            seasons[season]["Champions"][champion]["wins"] = raw_champions[season][champion]["wins"]
            seasons[season]["Champions"][champion]["losses"] = raw_champions[season][champion]["losses"]
            seasons[season]["Champions"][champion]["level"] = raw_champions[season][champion]["level"]
            seasons[season]["Champions"][champion]["points"] = raw_champions[season][champion]["points"]
            count_champions += 1
            if count_champions == 6:
                break
        if count == 3:
            break
    return seasons


def generate_matches_tab(db, profile, summoners):
    """
    :type db: darkarisulolstats.lolstats.database.Database
    """
    matches_tab = []
    raw_matches = db.preprocessed.get(profile, "matchlists")
    for raw_match in raw_matches:
        match = {"Season": raw_match["season"], "Champion": raw_match["champion"], "Role": raw_match["role"],
                 "Win": raw_match["win"], "Queue": raw_match["queue"], "Kills": raw_match["kills"],
                 "Deaths": raw_match["deaths"], "Assists": raw_match["assists"], "KDA": raw_match["kda"],
                 "CS": raw_match["cs"], "CS per min": raw_match["csPerMin"], "Date": raw_match["date"],
                 "Duration": raw_match["duration"], "Damage": raw_match["damage"]}
        matches_tab.append(match)
    return matches_tab


def generate_champions_tab(db, profile, summoners):
    """
    :type db: darkarisulolstats.lolstats.database.Database
    """
    champions_tab = {}
    raw_champions = db.preprocessed.get(profile, "champions")
    for season in raw_champions:
        if season not in champions_tab:
            champions_tab[season] = []
        for raw_champion in raw_champions[season]:
            champion = {}
            champion["Name"] = raw_champion
            for key in raw_champions[season][raw_champion].keys():
                champion[key.capitalize()] = raw_champions[season][raw_champion][key]
            champions_tab[season].append(champion)
    for season in champions_tab:
        champions_tab[season] = list(sorted(champions_tab[season], key=lambda i: i['Games']))
    return champions_tab

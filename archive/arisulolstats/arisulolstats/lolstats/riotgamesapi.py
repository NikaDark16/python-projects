import riotwatcher

import arisulolstats.constants as constants


class RiotGamesApi(riotwatcher.RiotWatcher):
    def __init__(self, api_key, custom_handler_chain=None, **kwargs):
        super(RiotGamesApi, self).__init__(api_key, custom_handler_chain, **kwargs)

    def summoner_by_name(self, summoner):
        region = constants.REGIONAL_ENDPOINTS[summoner["server"]].lower()
        name = summoner["name"]
        return self.summoner.by_name(region, name)

    def league_by_summoner(self, summoner, raw_summoner):
        region = constants.REGIONAL_ENDPOINTS[summoner["server"]].lower()
        encrypted_summoner_id = raw_summoner["id"]

        return self.league.by_summoner(region, encrypted_summoner_id)

    def champion_mastery_by_summoner(self, summoner, raw_summoner):
        region = constants.REGIONAL_ENDPOINTS[summoner["server"]].lower()
        encrypted_summoner_id = raw_summoner["id"]
        return self.champion_mastery.by_summoner(region, encrypted_summoner_id)

    def match_matchlist_by_account(self, summoner, raw_summoner, queue=None, begin_time=None, end_time=None,
                                   begin_index=None, end_index=None, season=None, champion=None):
        region = constants.REGIONAL_ENDPOINTS[summoner["server"]].lower()
        encrypted_account_id = raw_summoner["accountId"]
        return self.match.matchlist_by_account(region, encrypted_account_id, queue, begin_time, end_time, begin_index,
                                               end_index, season, champion)

    def match_by_id(self, server, game_id):
        region = constants.REGIONAL_ENDPOINTS[server].lower()
        return self.match.by_id(region, game_id)

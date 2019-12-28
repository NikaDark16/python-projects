import json
import sqlite3 as sql


class Database:
    def __init__(self):
        self.database = sql.connect("./data/data.db")
        self.cur = self.database.cursor()
        self.summoners = Summoners(self.cur)
        self.leagues = Leagues(self.cur)
        self.champion_masteries = ChampionMasteries(self.cur)
        self.matchlists = Matchlists(self.cur)
        self.data = Data(self.cur)
        self.cache_matches = self.data.get("matches")

        self.matches = Matches(self.cur, self.cache_matches)
        self.preprocessed = Preprocessed(self.cur)

    def __del__(self):
        self.data.add("matches", self.matches.get_cache_matches())
        self.database.commit()


class Summoners:
    def __init__(self, cur):
        self.cur = cur
        self.cur.execute(
            """CREATE TABLE IF NOT EXISTS summoners 
            (server TEXT NOT NULL, name TEXT NOT NULL, data TEXT NOT NULL)""")

    def check(self, summoner):
        server = summoner["server"]
        name = summoner["name"]
        self.cur.execute("SELECT 1 FROM summoners WHERE server = ? and name = ?", (server, name))
        if self.cur.fetchone() is not None:
            return True
        else:
            return False

    def add(self, summoner, data):
        if data:
            server = summoner["server"]
            name = summoner["name"]
            if self.check(summoner):
                self.cur.execute("UPDATE summoners SET data=? WHERE server = ? and name = ?",
                                 (json.dumps(data), server, name))
            else:
                self.cur.execute("INSERT INTO summoners VALUES(?, ?, ?)", (server, name, json.dumps(data)))

    def get(self, summoner):
        server = summoner["server"]
        name = summoner["name"]
        self.cur.execute("SELECT data FROM summoners WHERE server = ? and name = ?", (server, name))
        data = self.cur.fetchone()
        if data is None:
            return {}
        else:
            return json.loads(data[0])


class Leagues:
    def __init__(self, cur):
        self.cur = cur
        self.cur.execute(
            """CREATE TABLE IF NOT EXISTS leagues 
            (server TEXT NOT NULL, name TEXT NOT NULL, data TEXT NOT NULL)""")

    def check(self, summoner):
        server = summoner["server"]
        name = summoner["name"]
        self.cur.execute("SELECT 1 FROM leagues WHERE server = ? and name = ?", (server, name))
        if self.cur.fetchone() is not None:
            return True
        else:
            return False

    def add(self, summoner, data):
        if data:
            server = summoner["server"]
            name = summoner["name"]
            if self.check(summoner):
                self.cur.execute("UPDATE leagues SET data=? WHERE server = ? and name = ?",
                                 (json.dumps(data), server, name))
            else:
                self.cur.execute("INSERT INTO leagues VALUES(?, ?, ?)", (server, name, json.dumps(data)))

    def get(self, summoner):
        server = summoner["server"]
        name = summoner["name"]
        self.cur.execute("SELECT data FROM leagues WHERE server = ? and name = ?", (server, name))
        data = self.cur.fetchone()
        if data is None:
            return []
        else:
            return json.loads(data[0])


class ChampionMasteries:
    def __init__(self, cur):
        self.cur = cur
        self.cur.execute(
            """CREATE TABLE IF NOT EXISTS championMasteries
            (server TEXT NOT NULL, name TEXT NOT NULL, data TEXT NOT NULL)""")

    def check(self, summoner):
        server = summoner["server"]
        name = summoner["name"]
        self.cur.execute("SELECT 1 FROM championMasteries WHERE server = ? and name = ?", (server, name))
        if self.cur.fetchone() is not None:
            return True
        else:
            return False

    def add(self, summoner, data):
        if data:
            server = summoner["server"]
            name = summoner["name"]
            if self.check(summoner):
                self.cur.execute("UPDATE championMasteries SET data=? WHERE server = ? and name = ?",
                                 (json.dumps(data), server, name))
            else:
                self.cur.execute("INSERT INTO championMasteries VALUES(?, ?, ?)", (server, name, json.dumps(data)))

    def get(self, summoner):
        server = summoner["server"]
        name = summoner["name"]
        self.cur.execute("SELECT data FROM championMasteries WHERE server = ? and name = ?", (server, name))
        data = self.cur.fetchone()
        if data is None:
            return {}
        else:
            return json.loads(data[0])


class Matchlists:
    def __init__(self, cur):
        self.cur = cur
        self.cur.execute(
            """CREATE TABLE IF NOT EXISTS matchlists 
            (server TEXT NOT NULL, name TEXT NOT NULL, data TEXT NOT NULL)""")

    def check(self, summoner):
        server = summoner["server"]
        name = summoner["name"]
        self.cur.execute("SELECT 1 FROM matchlists WHERE server = ? and name = ?", (server, name))
        if self.cur.fetchone() is not None:
            return True
        else:
            return False

    def add(self, summoner, data):
        if data:
            server = summoner["server"]
            name = summoner["name"]
            if self.check(summoner):
                self.cur.execute("UPDATE matchlists SET data=? WHERE server = ? and name = ?",
                                 (json.dumps(data), server, name))
            else:
                self.cur.execute("INSERT INTO matchlists VALUES(?, ?, ?)", (server, name, json.dumps(data)))

    def get(self, summoner):
        server = summoner["server"]
        name = summoner["name"]
        self.cur.execute("SELECT data FROM matchlists WHERE server = ? and name = ?", (server, name))
        data = self.cur.fetchone()
        if data is None:
            return []
        else:
            return json.loads(data[0])


class Matches:
    def __init__(self, cur, cache_matches):
        self.cur = cur
        self.cache_matches = cache_matches
        self.cur.execute(
            """CREATE TABLE IF NOT EXISTS matches 
            (server TEXT NOT NULL, gameId INTEGER NOT NULL, data TEXT NOT NULL)""")

    def check(self, server, game_id):
        game_id_str = str(game_id)
        if server not in self.cache_matches:
            self.cache_matches[server] = {}
        if game_id_str not in self.cache_matches[server] or not self.cache_matches[server][game_id_str]:
            self.cur.execute("SELECT 1 FROM matches WHERE server = ? and gameId = ?", (server, game_id))
            if self.cur.fetchone() is None:
                self.cache_matches[server][game_id_str] = False
            else:
                self.cache_matches[server][game_id_str] = True
        return self.cache_matches[server][game_id_str]

    def add(self, server, game_id, data):
        if data:
            if self.check(server, game_id):
                self.cur.execute("UPDATE matches SET data=? WHERE server = ? and gameId = ?",
                                 (json.dumps(data), server, game_id))
            else:
                self.cur.execute("INSERT INTO matches VALUES(?, ?, ?)", (server, game_id, json.dumps(data)))

    def get(self, server, game_id):
        server = server
        game_id = game_id
        self.cur.execute("SELECT data FROM matches WHERE server = ? and gameId = ?", (server, game_id))
        data = self.cur.fetchone()
        if data is None:
            return []
        else:
            return json.loads(data[0])

    def get_cache_matches(self):
        return self.cache_matches


class Data:
    def __init__(self, cur):
        self.cur = cur
        self.cur.execute(
            """CREATE TABLE IF NOT EXISTS data 
            (name TEXT NOT NULL, data TEXT NOT NULL)""")

    def check(self, name):
        self.cur.execute("SELECT 1 FROM data WHERE name = ?", (name,))
        if self.cur.fetchone() is not None:
            return True
        else:
            return False

    def add(self, name, data):
        if data:
            if self.check(name):
                self.cur.execute("UPDATE data SET data=? WHERE name = ?",
                                 (json.dumps(data), name))
            else:
                self.cur.execute("INSERT INTO data VALUES(?, ?)", (name, json.dumps(data)))

    def get(self, name):
        self.cur.execute("SELECT data FROM data WHERE name = ?", (name,))
        data = self.cur.fetchone()
        if data is None:
            return {}
        else:
            return json.loads(data[0])


class Preprocessed:
    def __init__(self, cur):
        self.cur = cur
        self.cur.execute(
            """CREATE TABLE IF NOT EXISTS preprocessed 
            (profile TEXT NOT NULL, name TEXT NOT NULL, data TEXT NOT NULL)""")

    def check(self, profile, name):
        self.cur.execute("SELECT 1 FROM preprocessed WHERE profile = ? and name = ?", (profile, name))
        if self.cur.fetchone() is not None:
            return True
        else:
            return False

    def add(self, profile, name, data):
        if data:
            if self.check(profile, name):
                self.cur.execute("UPDATE preprocessed SET data=? WHERE profile = ? and name = ?",
                                 (json.dumps(data), profile, name))
            else:
                self.cur.execute("INSERT INTO preprocessed VALUES(?, ?, ?)", (profile, name, json.dumps(data)))

    def get(self, profile, name):
        self.cur.execute("SELECT data FROM preprocessed WHERE profile = ? and name = ?", (profile, name))
        data = self.cur.fetchone()
        if data is None:
            return {}
        else:
            return json.loads(data[0])

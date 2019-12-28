import PyQt5.QtCore as C
import PyQt5.QtGui as G
import PyQt5.QtWidgets as W


class Summoner(W.QWidget):
    def __init__(self, parent, data):
        super().__init__(parent)

        layout = W.QGridLayout(self)  # var
        group_summoner = GroupSummoner(self, data)  # var

        group_all_season = GroupSeason(self, data["seasons"]["all"], "All seasons")  # var

        try:
            group_last_season = GroupSeason(self, list(data["seasons"].values())[1],
                                        list(data["seasons"])[1] + " seasons")  # var
            layout.addWidget(group_last_season, 0, 2, 1, 1)  # set layout
        except:
            pass



        if len(data["seasons"]) > 2:
            group_seasons = []  # var
            for season in list(data["seasons"])[2:]:
                group_seasons.append(GroupSeason(self, data["seasons"][season], str(season) + " seasons"))
            for i in range(len(data["seasons"]) - 2):
                layout.addWidget(group_seasons[i], 1, i, 1, 1)  # set layout

        layout.addWidget(group_all_season, 0, 0, 1, 1)  # set layout
        layout.addWidget(group_summoner, 0, 1, 1, 1)  # set layout



class GroupSummoner(W.QGroupBox):
    def __init__(self, parent, data):
        super().__init__(parent)
        summoner = data["summoner"]
        layout = W.QGridLayout(self)  # var
        label_profile_icon = W.QLabel(self)  # var
        label_name = W.QLabel(summoner["name"], self)  # var
        label_level = W.QLabel("Level: " + str(summoner["level"]), self)  # var
        try:
            hour = int(summoner["Playtime"] / 60)
            minute = round(summoner["Playtime"] - (hour * 60))
            label_playtime = W.QLabel("Playtime: " + str(hour) + " h " + str(minute) + " m", self)  # var
            layout.addWidget(label_playtime, 2, 1)  # set layout
        except:
            pass
        vertical_spacer = W.QSpacerItem(20, 40, W.QSizePolicy.Minimum, W.QSizePolicy.Expanding)  # var
        horizontal_spacer = W.QSpacerItem(40, 20, W.QSizePolicy.Expanding, W.QSizePolicy.Minimum)  # var
        profile_icon = G.QPixmap(G.QImage(summoner["profileIconPath"]))  # var
        if data["leagues"]:
            group_leagues = GroupLeagues(self, data["leagues"])  # var

        self.setTitle("Summoner")  # set self
        #
        label_profile_icon.setPixmap(profile_icon.scaled(64, 64))  # set label_profile_icon

        label_name.setAlignment(C.Qt.AlignCenter)
        label_level.setAlignment(C.Qt.AlignCenter)
        label_profile_icon.setAlignment(C.Qt.AlignCenter)
        label_playtime.setAlignment(C.Qt.AlignCenter)

        layout.addWidget(label_name, 0, 1)  # set layout
        layout.addWidget(label_level, 1, 1)  # set layout
        layout.addWidget(label_profile_icon, 3, 1)  # set layout
        if data["leagues"]:
            layout.addWidget(group_leagues, 4, 1)  # set layout
        layout.addItem(vertical_spacer, 5, 1)
        layout.addItem(horizontal_spacer, 5, 0)
        layout.addItem(horizontal_spacer, 5, 2)


class GroupLeagues(W.QGroupBox):
    def __init__(self, parent, data):
        super().__init__(parent)

        layout = W.QGridLayout(self)  # var
        group_leagues = []  # var

        self.setTitle("Leagues")  # set self
        # self.setSizePolicy(W.QSizePolicy.Maximum, W.QSizePolicy.Maximum)

        for league in data:  # set group_leagues
            group_leagues.append(GroupLeague(self, data[league], league))

        for i in range(len(group_leagues)):
            layout.addWidget(group_leagues[i], 0, i)


class GroupLeague(W.QGroupBox):
    def __init__(self, parent, data, name):
        super().__init__(parent)

        layout = W.QGridLayout(self)  # var
        vertical_spacer = W.QSpacerItem(20, 40, W.QSizePolicy.Minimum, W.QSizePolicy.Expanding)  # var
        horizontal_spacer = W.QSpacerItem(40, 20, W.QSizePolicy.Expanding, W.QSizePolicy.Minimum)  # var
        label_league_icon = W.QLabel(self)  # var
        label_tier_rank = W.QLabel("{} {}".format(data["tier"], data["rank"]), self)  # var
        label_points_wins_losses = W.QLabel(
            "{} LP / {}W {}L {}G".format(data["points"], data["wins"], data["losses"], data["wins"] + data["losses"]),
            self)  # var
        label_win_ratio = W.QLabel(
            "Win Ratio {}%".format(round((data["wins"] / (data["wins"] + data["losses"])) * 10000) / 100),
            self)  # var

        league_icon = G.QPixmap(G.QImage(data["leagueIconPath"]))  # var

        self.setTitle(name)  # set self

        label_league_icon.setPixmap(league_icon.scaled(96, 96))  # set label_profile_icon

        layout.addWidget(label_league_icon, 0, 0, 3, 1)
        layout.addWidget(label_tier_rank, 0, 1)
        layout.addWidget(label_points_wins_losses, 1, 1)
        layout.addWidget(label_win_ratio, 2, 1)
        layout.addItem(vertical_spacer, 3, 0)  # set layout
        layout.addItem(horizontal_spacer, 0, 2)  # set layout


class GroupSeason(W.QGroupBox):
    def __init__(self, parent, data, name):
        super().__init__(parent)

        layout = W.QGridLayout(self)  # var
        vertical_spacer = W.QSpacerItem(20, 40, W.QSizePolicy.Minimum, W.QSizePolicy.Expanding)  # var
        horizontal_spacer = W.QSpacerItem(40, 20, W.QSizePolicy.Expanding, W.QSizePolicy.Minimum)  # var
        roles = []  # var
        champions = []  # var
        champions_icon = []  # var
        champions_icon_images = []  # var

        self.setTitle(name)  # set self

        for champion in data["Champions"]:
            champions.append(GroupSeasonCell(self, data["Champions"][champion], champion))
            champions_icon.append(W.QLabel(self))
            champions_icon_images.append(G.QPixmap(G.QImage(data["Champions"][champion]["iconPath"])))  # var
            champions_icon[-1].setPixmap(champions_icon_images[-1].scaled(32, 32))
            champions_icon[-1].setAlignment(C.Qt.AlignCenter)
        roles.append(GroupSeasonCell(self, data["All"], "All roles"))
        for role in data["Roles"]:
            if role != "None":
                roles.append(GroupSeasonCell(self, data["Roles"][role], role))

        before_champions = int(round((len(champions_icon) / 2) + 0.25))  # var
        before_roles = int(round((len(roles) / 2) + 0.25))  # var

        line = W.QFrame(self)
        line.setFrameShape(W.QFrame.HLine)
        line.setFrameShadow(W.QFrame.Sunken);


        for i in range(before_champions):
            layout.addWidget(champions_icon[i], 3, i + 1)  # set layout
            layout.addWidget(champions[i], 4, i + 1)  # set layout
        for i in range(before_champions, len(champions)):
            layout.addWidget(champions_icon[i], 5, i + 1 - before_champions)  # set layout
            layout.addWidget(champions[i], 6, i + 1 - before_champions)  # set layout
        for i in range(before_roles):
            layout.addWidget(roles[i], 0, i + 1)  # set layout
        for i in range(before_roles, len(roles)):
            layout.addWidget(roles[i], 1, i + 1 - before_roles)  # set layout

        if before_champions > before_roles:
            horizontal_spacer_size = before_champions
        else:
            horizontal_spacer_size = before_roles
        layout.addItem(vertical_spacer, 7, 0)  # set layout
        layout.addItem(horizontal_spacer, 0, 0)  # set layout
        layout.addItem(horizontal_spacer, 0, horizontal_spacer_size + 1)  # set layout
        layout.addWidget(line, 2, 0, 1, horizontal_spacer_size + 2)

class GroupSeasonCell(W.QLabel):
    def __init__(self, parent, data, name):
        super().__init__(parent)
        if "level" in data:
            self.setText(
                "{}({} lvl)\n{:,d} pts\n{}W {}L {}G\nWin Ratio {}%".format(name, data["level"], data["points"],
                                                                           data["wins"],
                                                                           data["losses"],
                                                                           data["wins"] + data["losses"], round(
                        (data["wins"] / (data["wins"] + data["losses"])) * 10000) / 100))
        else:
            self.setText("{}\n{}W {}L {}G\nWin Ratio {}%".format(name, data["wins"], data["losses"],
                                                                 data["wins"] + data["losses"], round(
                    (data["wins"] / (data["wins"] + data["losses"])) * 10000) / 100))
        self.setAlignment(C.Qt.AlignCenter)

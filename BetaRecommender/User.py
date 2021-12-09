import pandas as pd


class User:
    def __init__(self, gn, g, t):  # self, game_names, genres, themes):
        '''
        self.name = input("Name: ")
        self.game_names = input(
            "List some game names(s) with commas and no spaces: ").split(",")
        self.genres = input(
            "List your genre(s) with commas and no spaces: ").split(",")
        self.themes = input(
            "List some themes with commas and no spaces: ").split(",")
        '''
        self.name = "TESTer"
        self.game_names = pd.Series(gn)
        self.genres = pd.Series(g)
        self.themes = pd.Series(t)

        self.series = pd.Series(data=[self.name, self.game_names, self.genres, self.themes],
                                index=["user", "game_names", "genres", "themes"])

    def printUser(self):
        print(self.name, "'s profile:\n- ", self.game_names,
              "\n- ", self.genres, "\n-", self.themes)

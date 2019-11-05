
class Tennis:
    INITIAL_NUMBER_OF_TEAMS = 2
    INITIAL_NUMBER_OF_PLAYERS = 1

    def __init__(self, number_of_players_per_team = INITIAL_NUMBER_OF_PLAYERS):
        self.__number_of_players_per_team = number_of_players_per_team

    def number_of_teams(self):
        return self.INITIAL_NUMBER_OF_TEAMS

    def team_1_number_of_players(self):
        return self.__number_of_players_per_team

    def team_2_number_of_players(self):
        return self.__number_of_players_per_team

    def score(self):
        return (0,0,0)
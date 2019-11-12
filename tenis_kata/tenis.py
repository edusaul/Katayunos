class Game:

    DEFAULT_NUMBER_OF_PLAYERS=1

    def __init__(self,number_of_players=DEFAULT_NUMBER_OF_PLAYERS):
        self.__number_of_players=number_of_players

    def are_two_teams(self):
        return 2

    def get_number_of_players(self):
        return self.__number_of_players

    def number_of_players_team_1(self):
        return self.get_number_of_players()

    def number_of_players_team_2(self):
        return self.get_number_of_players()
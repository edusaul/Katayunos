import unittest
from Tennis.Tennis_rules import Tennis

class MyTestCase(unittest.TestCase):
    def test_there_are_teams(self):

        initial_number_of_teams = 2
        game = Tennis()

        teams = game.number_of_teams()

        self.assertEqual(teams, initial_number_of_teams)

    def test_teams_have_same_number_of_players(self):

        game = Tennis()

        team1_number_of_players = game.team_1_number_of_players()
        team2_number_of_players = game.team_2_number_of_players()

        self.assertEqual(team1_number_of_players,team2_number_of_players)

    def test_teams_have_1_player(self):

        number_of_players_per_team = 1
        game = Tennis(number_of_players_per_team)

        team1_number_of_players = game.team_1_number_of_players()
        team2_number_of_players = game.team_2_number_of_players()

        self.assertEqual(team1_number_of_players,number_of_players_per_team)
        self.assertEqual(team2_number_of_players,number_of_players_per_team)

    def test_teams_have_2_players(self):

        number_of_players_per_team = 2
        game = Tennis(number_of_players_per_team)

        team1_number_of_players = game.team_1_number_of_players()
        team2_number_of_players = game.team_2_number_of_players()

        self.assertEqual(team1_number_of_players,number_of_players_per_team)
        self.assertEqual(team2_number_of_players,number_of_players_per_team)

    def test_teams_start_0_points_0_sets_0_games(self):

        game = Tennis()
        score = game.score()

        score['team1']

        self.assertEqual(team1_points,0)
        self.assertEqual(team1_sets,0)
        self.assertEqual(team1_games,0)


if __name__ == '__main__':
    unittest.main()

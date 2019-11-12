import unittest
from tenis_kata.tenis import Game


class MyTestCase(unittest.TestCase):
    def test_are_two_teams(self):

        game = Game()

        are_two_teams = game.are_two_teams()

        self.assertEqual(are_two_teams, 2)

    def test_is_one_player_at_least(self):

        game = Game(1)

        number_of_players = game.get_number_of_players()

        self.assertGreater(number_of_players, 0)

    def test_is_max_two_players(self):

        game = Game()

        number_of_players = game.get_number_of_players()

        self.assertLess(number_of_players, 3)

    def test_is_same_number_of_players_in_each_team(self):

        game = Game()

        number_of_players_team_1 = game.number_of_players_team_1()
        number_of_players_team_2 = game.number_of_players_team_2()

        self.assertEqual(number_of_players_team_1, number_of_players_team_2)

if __name__ == '__main__':
    unittest.main()

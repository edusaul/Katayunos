import unittest
from Tennis_3.tennis_game import Game

class MyTestCase(unittest.TestCase):
    INITIAL_POINTS = "love"
    def test_game_start_with_0_points(self):

        game = Game()
        team1=1
        team2=2

        points_team1 = game.points(team1)
        points_team2 = game.points(team2)

        self.assertEqual(points_team1, self.INITIAL_POINTS)
        self.assertEqual(points_team2, self.INITIAL_POINTS)

    def test_score_points(self):

        game = Game()

        team = 1

        game.score(team)
        points = game.points(team)

        self.assertEqual(points,"Fifteen")

        game.score(team)
        points = game.points(team)

        self.assertEqual(points,"Thirty")

        game.score(team)
        points = game.points(team)

        self.assertEqual(points,"Forty")


if __name__ == '__main__':
    unittest.main()

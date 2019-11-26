import unittest
from Tennis_4.tennis import Game

class MyTestCase(unittest.TestCase):
    STARTING_POINTS = 0
    STARTING_GAMES = 0
    STARTING_SETS = 0
    POINT_NAMES=['love', 'fifteen', 'thirty', 'forty']
    def test_teams_starts_with_0_points(self):

        game = Game()

        team1_points = game.points(1)
        team2_points = game.points(2)

        self.assertEqual(team1_points, self.STARTING_POINTS)
        self.assertEqual(team2_points, self.STARTING_POINTS)

    def test_sets_and_games_starts_with_0_points(self):

        game = Game()

        team1_sets = game.sets(1)
        team2_sets = game.sets(2)
        team1_games = game.games(1)
        team2_games = game.games(2)

        self.assertEqual(team1_sets, self.STARTING_SETS)
        self.assertEqual(team2_sets, self.STARTING_SETS)
        self.assertEqual(team1_games, self.STARTING_GAMES)
        self.assertEqual(team2_games, self.STARTING_GAMES)

    def test_point_names(self):

        game = Game()

        points0 = game.name_points(0)
        points1 = game.name_points(1)
        points2 = game.name_points(2)
        points3 = game.name_points(3)

        self.assertEqual(points0, self.POINT_NAMES[0])
        self.assertEqual(points1, self.POINT_NAMES[1])
        self.assertEqual(points2, self.POINT_NAMES[2])
        self.assertEqual(points3, self.POINT_NAMES[3])

    def test_score_points(self):
        game=Game()

        game.score(1)
        points=game.name_points(game.points(1))
        self.assertEqual(points,self.POINT_NAMES[1])



if __name__ == '__main__':
    unittest.main()

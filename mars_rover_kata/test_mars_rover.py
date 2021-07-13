import unittest


class MarsRover:
    def __init__(self, initial_position):
        self._position = initial_position

    def execute(self, command):
        if command == "M":
            if self._position[2] == "N":
                self._position = (self._position[0], self._position[1] + 1, self._position[2])
            elif self._position[2] == "E":
                self._position = (self._position[0] + 1, self._position[1], self._position[2])
            elif self._position[2] == "W":
                self._position = (self._position[0] - 1, self._position[1], self._position[2])
            elif self._position[2] == "S":
                self._position = (self._position[0], self._position[1] - 1, self._position[2])

    def final_position(self):
        return self._position


class MarsRoverTests(unittest.TestCase):
    def test_rover_knows_landing_point(self):
        landing_point = (5, 5, "N")
        rover = MarsRover(landing_point)
        rover.execute("")
        position = rover.final_position()
        expected_position = landing_point

        self.assertEqual(expected_position, position)

    def test_moves_forward_once_oriented_N(self):
        landing_point = (1, 2, "N")
        rover = MarsRover(landing_point)
        rover.execute("M")
        position = rover.final_position()
        expected_position = (1, 3, "N")

        self.assertEqual(expected_position, position)

    def test_moves_forward_once_oriented_E(self):
        landing_point = (1, 2, "E")
        rover = MarsRover(landing_point)
        rover.execute("M")
        position = rover.final_position()
        expected_position = (2, 2, "E")

        self.assertEqual(expected_position, position)

    def test_moves_forward_once_oriented_W(self):
        landing_point = (1, 2, "W")
        rover = MarsRover(landing_point)
        rover.execute("M")
        position = rover.final_position()
        expected_position = (0, 2, "W")

        self.assertEqual(expected_position, position)

    def test_moves_forward_once_oriented_S(self):
        landing_point = (1, 2, "S")
        rover = MarsRover(landing_point)
        rover.execute("M")
        position = rover.final_position()
        expected_position = (1, 1, "S")

        self.assertEqual(expected_position, position)


if __name__ == '__main__':
    unittest.main()

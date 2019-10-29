from new_scuba.Scuba_Diver import ScubaDiver

import unittest


class TestScubaDiver(unittest.TestCase):
    SEA_LEVEL = 0
    def test_starts_full_oxygen(self):

        full_oxygen = 150

        scuba = ScubaDiver()

        self.assertEqual(scuba.oxygen, full_oxygen)

    def test_starts_in_sea_level(self):

        scuba = ScubaDiver()

        self.assertEqual(scuba.depth, self.SEA_LEVEL)

    def test_starts_alive(self):

        is_alive = True

        scuba = ScubaDiver()

        self.assertEqual(scuba.is_alive, is_alive)

    def test_can_hold_depth_level(self):

        scuba = ScubaDiver()

        scuba.hold_depth()

        self.assertEqual(scuba.depth, self.SEA_LEVEL)

    def test_can_dive(self):

        scuba = ScubaDiver()

        scuba.dive()

        self.assertEqual(scuba.depth, self.SEA_LEVEL-1)

    def test_can_ascend(self):

        scuba = ScubaDiver()
        scuba.dive()
        final_depth = self.SEA_LEVEL

        scuba.ascend()

        self.assertEqual(scuba.depth, final_depth)

    def test_can_not_ascend_over_sea_level(self):

        scuba = ScubaDiver()

        scuba.ascend()

        self.assertEqual(scuba.depth, self.SEA_LEVEL)

    def test_start_without_points(self):

        scuba = ScubaDiver()

        self.assertEqual(scuba.score(), 0)





if __name__ == '__main__':
    unittest.main()

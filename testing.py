import unittest
from first import mysum


class TestSum(unittest.TestCase):
    def test_sum(self):
        self.assertEqual(mysum(3, 6), 9, "Should be 9")

    def test_sum_2(self):
        self.assertEqual(mysum(-2, 2), 0, "Should be 0")


if __name__ == '__main__':
    unittest.main()

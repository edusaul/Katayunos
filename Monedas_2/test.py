import unittest
from Monedas_2.CoinConversor import CoinConversor


class MyTestCase(unittest.TestCase):
    def test_1euro_returns_1coin_of_1e(self):

        expected = "1 coin of 1€"
        coin_conversor = CoinConversor(1)

        result = coin_conversor.write()

        self.assertEqual(expected, result)

    def test_2euro_retuns_1_coin_of_2e(self):

        expected = "1 coin of 2€"
        coin_conversor = CoinConversor(2)

        result = coin_conversor.write()

        self.assertEqual(expected, result)

    def test_3euro_retuns_1_coin_of_2e_and_1_coin_of_1e(self):

        expected = "1 coin of 2€, 1 coin of 1€"
        coin_conversor = CoinConversor(3)

        result = coin_conversor.write()

        self.assertEqual(expected, result)

    def test_27euro_retuns_13_coins_of_2e_and_1_coin_of_1e(self):

        expected = "13 coins of 2€, 1 coin of 1€"
        coin_conversor = CoinConversor(27)

        result = coin_conversor.write()

        self.assertEqual(expected, result)


if __name__ == '__main__':
    unittest.main()

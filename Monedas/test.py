import unittest


class MyTestCase(unittest.TestCase):
    def test_given_1_euro_returns_1e_coin(self):

        amount_given = 1
        coin_conversor = CoinConversor()

        coins = coin_conversor.calculate_coins(amount_given)

        self.assertEqual("1x1€", coins)

    def test_given_2_euro_returns_2e_coin(self):

        amount_given = 2
        coin_conversor = CoinConversor()

        coins = coin_conversor.calculate_coins(amount_given)

        self.assertEqual("1x2€", coins)

    def test_given_4_euro_returns_2_coins_of_2e(self):

        amount_given = 4
        coin_conversor = CoinConversor()

        coins = coin_conversor.calculate_coins(amount_given)

        self.assertEqual("2x2€", coins)

    def test_given_3_euro_returns_1x2e_and_1x1e_coins(self):

        amount_given = 3
        coin_conversor = CoinConversor()

        coins = coin_conversor.calculate_coins(amount_given)

        self.assertEqual("1x2€ 1x1€", coins)

    def test_given_223_euro_returns_111x2e_and_1x1e_coins(self):

        amount_given = 223
        coin_conversor = CoinConversor()

        coins = coin_conversor.calculate_coins(amount_given)

        self.assertEqual("111x2€ 1x1€", coins)


if __name__ == '__main__':
    unittest.main()


class CoinConversor:
    def calculate_coins(self, amount):
        coins = ""
        num_2e_coins = int(amount/2)
        if num_2e_coins > 0:
            coins = str(num_2e_coins)+"x2€"
        if not self.is_divisible_by_2(amount):
            if coins != "":
                coins += " "
            coins += "1x1€"
        return coins

    def is_divisible_by_2(self,amount):
        if amount%2 == 0:
            return True
        return False
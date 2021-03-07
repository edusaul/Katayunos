import unittest

from Poker_Hands.poker_hands import PokerHands

class MyTestCase(unittest.TestCase):
    def test_compare_the_value_of_two_cards(self):
        poker_hands = PokerHands()

        first_card = '2'
        second_card = '3'
        result = poker_hands.compare_two_cards(first_card, second_card)

        self.assertEqual('3', result)

        first_card = 'K'
        second_card = '3'
        result = poker_hands.compare_two_cards(first_card, second_card)

        self.assertEqual('K', result)

        first_card = 'Q'
        second_card = 'K'
        result = poker_hands.compare_two_cards(first_card, second_card)

        self.assertEqual('K', result)

        first_card = 'A'
        second_card = 'J'
        result = poker_hands.compare_two_cards(first_card, second_card)

        self.assertEqual('A', result)

    def test_get_higher_value_from_set_of_cards(self):
        poker_hands = PokerHands()

        set_of_cards = ['2', 'A', 'J', '4', '5']

        result = poker_hands.compare_set_of_cards(set_of_cards)

        self.assertEqual('A', result)


if __name__ == '__main__':
    unittest.main()

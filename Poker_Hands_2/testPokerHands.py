import unittest
from Poker_Hands_2.pokerHands import PokerHands
from Poker_Hands_2.pokerHands import WrongNumberOfCardsException

class MyTestCase(unittest.TestCase):
    def test_can_set_a_hand_for_player(self):
        poker_hands = PokerHands(2)
        hand_1 = ["2H","3S","5C","JH","KS"]

        player = 1
        poker_hands.set_hand(player, hand_1)

        self.assertEqual(hand_1, poker_hands.get_hand(player))

    def test_player_have_5_cards(self):
        poker_hands = PokerHands(2)
        hand_1 = ["2H","3S","5C","JH"]

        player = 1

        self.assertRaises(WrongNumberOfCardsException, lambda: poker_hands.set_hand(player, hand_1))


if __name__ == '__main__':
    unittest.main()

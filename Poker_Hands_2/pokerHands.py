class WrongNumberOfCardsException(Exception):
    pass


class PokerHands:
    def __init__(self, number_of_players):
        self._players = [0] * number_of_players

    def set_hand(self, player, hand):
        if len(hand) != 5:
            raise WrongNumberOfCardsException('You must provide 5 cards for the hand')
        self._players[player-1] = hand

    def get_hand(self, player):
        return self._players[player-1]
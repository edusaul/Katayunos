import functools


class PokerHands:
    def __init__(self):
        self._card_values = ['2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A']

    def compare_criterium(self, first_card, second_card):
        first_index = self._card_values.index(first_card)
        second_index = self._card_values.index(second_card)

        if first_index > second_index:
            return 1
        elif first_index < second_index:
            return -1
        else:
            return 0

    def compare_two_cards(self, first_card, second_card):
        result = self.compare_criterium(first_card, second_card)
        if result == 1:
            return first_card
        return second_card

    def compare_set_of_cards(self, set_of_cards):

        sorted_array = sorted(set_of_cards, key=functools.cmp_to_key(self.compare_criterium), reverse=True)

        return sorted_array[0]

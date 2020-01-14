class RomanConversor(object):
    def convert_to_roman(self, number):
        if number == 4:
            return "IV"
        if number >= 5:
            return "V" + (number-5)*"I"
        return number*"I"

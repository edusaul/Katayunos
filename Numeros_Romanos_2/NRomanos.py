
class ArabicNumber:
    def __init__(self,number):
        self.number = number
        self.roman = ""
        self.roman_numbers = {10:"X", 9:"IX", 5:"V", 4:"IV"}

    def to_roman(self):
        for arabic, roman in self.roman_numbers.items():
            self.convert(arabic, roman)

        return self.roman + "I"*self.number

    def convert(self, number, letters):
        while self.number >= number:
            self.roman += letters
            self.number -= number

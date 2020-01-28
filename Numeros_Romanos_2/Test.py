import unittest
from Numeros_Romanos_2.NRomanos import ArabicNumber

class TestArabicNumber(unittest.TestCase):
    def test_convert_1_to_roman(self):

        roman_number = ArabicNumber(1).to_roman()

        self.assertEqual("I", roman_number)

    def test_convert_2_to_roman(self):

        roman_number = ArabicNumber(2).to_roman()

        self.assertEqual("II", roman_number)

    def test_convert_4_to_roman(self):

        roman_number = ArabicNumber(4).to_roman()

        self.assertEqual("IV", roman_number)

    def test_convert_5_to_roman(self):

        roman_number = ArabicNumber(5).to_roman()

        self.assertEqual("V", roman_number)

    def test_convert_6_to_roman(self):

        roman_number = ArabicNumber(6).to_roman()

        self.assertEqual("VI", roman_number)

    def test_convert_9_to_roman(self):

        roman_number = ArabicNumber(9).to_roman()

        self.assertEqual("IX", roman_number)

    def test_convert_10_to_roman(self):

        roman_number = ArabicNumber(10).to_roman()

        self.assertEqual("X", roman_number)

    def test_convert_11_to_roman(self):

        roman_number = ArabicNumber(11).to_roman()

        self.assertEqual("XI", roman_number)

    def test_convert_15_to_roman(self):

        roman_number = ArabicNumber(15).to_roman()

        self.assertEqual("XV", roman_number)

    def test_convert_19_to_roman(self):

        roman_number = ArabicNumber(19).to_roman()

        self.assertEqual("XIX", roman_number)

    def test_convert_20_to_roman(self):

        roman_number = ArabicNumber(20).to_roman()

        self.assertEqual("XX", roman_number)

    def test_convert_25_to_roman(self):

        roman_number = ArabicNumber(25).to_roman()

        self.assertEqual("XXV", roman_number)

if __name__ == '__main__':
    unittest.main()

import unittest
from Numeros_Romanos.NRomanos import RomanConversor


class MyTestCase(unittest.TestCase):
    def test_1_is_I(self):
        roman_conversor = RomanConversor()
        arabic_number = 1

        roman_number = roman_conversor.convert_to_roman(arabic_number)

        self.assertEqual("I", roman_number)

    def test_2_is_II(self):
        roman_conversor = RomanConversor()
        arabic_number = 2

        roman_number = roman_conversor.convert_to_roman(arabic_number)

        self.assertEqual("II", roman_number)

    def test_3_is_III(self):
        roman_conversor = RomanConversor()
        arabic_number = 3

        roman_number = roman_conversor.convert_to_roman(arabic_number)

        self.assertEqual("III", roman_number)

    def test_4_is_IV(self):
        roman_conversor = RomanConversor()
        arabic_number = 4

        roman_number = roman_conversor.convert_to_roman(arabic_number)

        self.assertEqual("IV", roman_number)

    def test_5_is_V(self):
        roman_conversor = RomanConversor()
        arabic_number = 5

        roman_number = roman_conversor.convert_to_roman(arabic_number)

        self.assertEqual("V", roman_number)

    def test_6_7_8_is_working(self):
        roman_conversor = RomanConversor()
        arabic_numbers = [6,7,8]
        roman_numbers=[]

        for arabic_number in arabic_numbers:
            roman_number = roman_conversor.convert_to_roman(arabic_number)
            roman_numbers.append(roman_number)

        self.assertEqual(["VI","VII","VIII"], roman_numbers)


if __name__ == '__main__':
    unittest.main()

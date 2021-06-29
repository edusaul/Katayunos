import unittest

from string_calculator.string_calculator_program import StringCalculator


class StringCalculatorTests(unittest.TestCase):
    def setUp(self) -> None:
        self.calculator = StringCalculator()

    def test_returns_0_with_empty_string(self):
        expected_for_empty_string = 0
        empty_string = ""

        result = self.calculator.calculate(empty_string)

        self.assertEqual(expected_for_empty_string, result)

    def test_returns_value_for_string_with_1_number(self):
        expected_result_for_some_number = 7
        some_number = "7"

        result = self.calculator.calculate(some_number)

        self.assertEqual(expected_result_for_some_number, result)

    def test_returns_sum_of_2_numbers(self):
        expected_result_for_two_numbers = 14
        some_numbers_to_sum = "8,6"

        result = self.calculator.calculate(some_numbers_to_sum)

        self.assertEqual(expected_result_for_two_numbers, result)

if __name__ == '__main__':
    unittest.main()

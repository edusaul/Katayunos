class StringCalculator:
    def calculate(self, string):
        result = 0
        if string != "":
            numbers = string.split(",")
            for number in numbers:
                result += int(number)

        return result


class TextProcessor:
    def __init__(self, text):
        self.__text = text

    def is_there(self, word):
        return word in self.__text

class Text_processor:
    def __init__(self):
        self.__text = ""

    def setText(self, text):
        self.__text = text

    def getText(self):
        return self.__text

    def search(self, word):
        return self.__text.find(word)

    def number_of_entries(self, word):
        return self.__text.count(word)


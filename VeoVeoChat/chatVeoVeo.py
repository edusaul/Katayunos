class ChatBot:
    BASE_MESSAGE = "veo veo una cosita que empieza por la letrita "
    def __init__(self):
        self.word = None

    def request(self, user, message):
        if self.word == None:
            words = message.split(" ")
            self.word = words[-1]
            letter = self.word[0].upper()
            return self.BASE_MESSAGE + letter



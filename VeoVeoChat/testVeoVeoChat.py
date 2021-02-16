import unittest
from VeoVeoChat.chatVeoVeo import ChatBot


class MyTestCase(unittest.TestCase):
    def test_bot_starts_game_for_1_player(self):
        user = 'pepe'
        message = '@chatbot veoveo camisa'
        expected = "veo veo una cosita que empieza por la letrita C"
        chat_bot = ChatBot()

        answer = chat_bot.request(user, message)

        self.assertEqual(expected, answer)

    def test_user_fails_to_answer(self):
        user = "pepe"
        message = "@chatbot veoveo camisa"
        chat_bot = ChatBot()
        chat_bot.request(user, message)
        user2 = "rafa"
        messageUser2 = "@chatbot paleta"
        expected = "@rafa has fallado"

        answer = chat_bot.request(user2, messageUser2)

        self.assertEqual(expected, answer)


if __name__ == '__main__':
    unittest.main()

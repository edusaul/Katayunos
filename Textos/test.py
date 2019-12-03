import unittest
from Textos.Texto import Text_processor

class MyTestCase(unittest.TestCase):
    TEXT = "La astronomía (del latín astronomĭa, y este del griego ἀστρονομία) es la ciencia que se ocupa del estudio de los cuerpos celestes del universo, incluidos los planetas y sus satélites, los cometas y meteoroides, las estrellas y la materia interestelar, los sistemas de materia oscura, estrellas, gas y polvo llamados galaxias y los cúmulos de galaxias; por lo que estudia sus movimientos y los fenómenos ligados a ellos. Su registro y la investigación de su origen viene a partir de la información que llega de ellos a través de la radiación electromagnética o de cualquier otro medio"
    def test_there_is_a_text(self):

        text_processor = Text_processor()
        text_processor.setText(self.TEXT)

        self.assertEqual(self.TEXT, text_processor.getText())

    def test_if_word_is_in_text(self):

        text_processor = Text_processor()
        text_processor.setText(self.TEXT)
        word = "cometas"

        position = text_processor.search(word)

        self.assertLessEqual(0, position)

        word = "hdsjkhasjkdka"

        position = text_processor.search(word)

        self.assertEqual(-1, position)

    def test_all_entries_of_a_word_in_text(self):
        text_processor = Text_processor()
        text_processor.setText(self.TEXT)
        word = "cometas"

        number_of_entries = text_processor.number_of_entries(word)

        self.assertLessEqual(0, number_of_entries)






if __name__ == '__main__':
    unittest.main()

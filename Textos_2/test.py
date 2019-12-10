import unittest
from Textos_2.procesador_texto import TextProcessor

class MyTestCase(unittest.TestCase):
    def test_buscar_si_palabra_esta_en_texto(self):

        text = "hola mundo"
        processor = TextProcessor(text)
        word_to_search = "mundo"

        is_there = processor.is_there(word_to_search)

        self.assertEqual(True, is_there)


    def test_comprobar_palabra_no_esta_en_texto(self):
        text = "hola mundo"
        processor = TextProcessor(text)
        word_to_search = "patata"

        is_there = processor.is_there(word_to_search)

        self.assertEqual(False, is_there)


    def test_comprobar_que_no_encuentra_solo_un_caracter(self):
        text = "hola mundo"
        processor = TextProcessor(text)
        word_to_search = "m"

        is_there = processor.is_there(word_to_search)

        self.assertEqual(False, is_there)

if __name__ == '__main__':
    unittest.main()

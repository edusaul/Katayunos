import unittest
from Potter_Books.Books import PotterBooks


class MyTestCase(unittest.TestCase):
    def test_buy_first_book(self):

        books_we_are_buying = {"1":1}
        potter_books = PotterBooks(books_we_are_buying)

        total = potter_books.price()

        self.assertEqual(8, total)

    def test_buy_two_copies_of_first_book(self):

        books_we_are_buying = {"1":2}
        potter_books = PotterBooks(books_we_are_buying)

        total = potter_books.price()

        self.assertEqual(16, total)

    def test_buy_books_first_and_second(self):

        books_we_are_buying = {"1":1, "2":1}
        potter_books = PotterBooks(books_we_are_buying)

        total = potter_books.price()

        self.assertEqual(15.2, total)


if __name__ == '__main__':
    unittest.main()




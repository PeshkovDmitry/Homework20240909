import unittest
from Package02.BookNotFoundError import BookNotFoundError
from Package02.Library import Library


class TestLibrary(unittest.TestCase):

    def test_adding(self):
        library = Library()
        library.add_book("Робинзон Крузо")
        self.assertIn("Робинзон Крузо", library.list_books(), "Книга не добавляется в библиотеку")

    def test_deleting(self):
        library = Library()
        library.add_book("Робинзон Крузо")
        library.remove_books("Робинзон Крузо")
        self.assertNotIn("Робинзон Крузо", library.list_books(), "Книга не добавляется в библиотеку")

    def test_deleting_unknown_book(self):
        library = Library()
        self.assertRaises(BookNotFoundError, library.remove_books, "Робинзон Крузо")

    def test_multiple_adding(self):
        library = Library()
        library.add_book("Робинзон Крузо")
        library.add_book("Алиса в стране чудес")
        self.assertEqual(len(library.list_books()), 2, "Количество книг не совпадает")
        self.assertIn("Робинзон Крузо", library.list_books(), "Книга не добавляется в библиотеку")
        self.assertIn("Алиса в стране чудес", library.list_books(), "Книга не добавляется в библиотеку")


if __name__ == "__main__":
    unittest.main()

import unittest
from library import Library, Book

class TestLibrary(unittest.TestCase):
    def test_add_single_book(self):
        library = Library()
        book = Book(isbn='1234567890', title='Test-Driven Development', author='xyz', year=2002)
        library.add_book(book)
        self.assertEqual(library.books[0].isbn, '1234567890')

if __name__ == '__main__':
    unittest.main()

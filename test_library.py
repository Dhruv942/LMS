import unittest
from library import Library, Book

class TestLibrary(unittest.TestCase):

    def setUp(self):
        self.library = Library()
    def test_add_single_book(self):
        library = Library()
        book = Book(isbn='1234567890', title='Test-Driven Development', author='xyz', year=2002)
        library.add_book(book)
        self.assertEqual(library.books[0].isbn, '1234567890')

    def test_add_multiplebook(self):
        library = Library()
        book1 = Book(isbn='1234567890', title='Test-Driven Development', author='xyz', year=2002)
        book2 = Book(isbn='123456789', title='python', author='abc', year=2002)
        library.add_book(book1)
        library.add_book(book2)
        self.assertEqual(library.books[0].isbn, '1234567890')
        self.assertEqual(library.books[1].isbn, '123456789')

    def test_add_duplicatebook(self):
        library = Library()
        book = Book(isbn='1234567890', title='Test-Driven Development', author='xyz', year=2002)
    
        library.add_book(book)  
        try:
            library.add_book(book)  
            self.fail("Expected ValueError not raised")
        except ValueError as e:
           self.assertEqual(str(e), "Book already in the library.")


    def test_borrowbook(self):
        book = Book(isbn="1234567890", title="c++", author="bde", year=2010)
        self.library.add_book(book)
        self.library.borrow_book(book.isbn)
        self.assertTrue(book.is_borrowed)

    def test_add_book_with_empty_fields(self):
        library = Library()
        book= Book(isbn='1234567891', title='Title', author='', year=2024)
        try:
            library.add_book(book)
            self.fail("Expected ValueError not raised for empty author")
        except ValueError as e:
           self.assertEqual(str(e), "Book author cannot be empty")

    def test_borrow_unavailable_book(self):
        book = Book(isbn="1234567890", title="c++", author="bde", year=2010)
        self.library.add_book(book)
        self.library.borrow_book(book.isbn)
        with self.assertRaises(ValueError):
            self.library.borrow_book(book.isbn)       

    def test_borrow_nonexistent_book(self):
        with self.assertRaises(ValueError):
            self.library.borrow_book("xyz")
            
if __name__ == '__main__':
    unittest.main()

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
            
    def test_return_book(self):
        book = Book(isbn="1234567890", title="snake", author="abc", year=1958)
        self.library.add_book(book)
        self.library.borrow_book(book.isbn)
        self.library.return_book(book.isbn)
        self.assertFalse(book.is_borrowed)

    def test_return_book_not_borrowed(self):
        book = Book(isbn="1234567890", title="snake", author="abc", year=1958)
        self.library.add_book(book)
        with self.assertRaises(ValueError):
            self.library.return_book(book.isbn)

    def test_get_available_books_all_borrowed(self):
        book1 = Book(isbn='1234567890', title='Test-Driven Development', author='xyz', year=2002)
        book2 = Book(isbn='123456789', title='Python', author='abc', year=2002)
        self.library.add_book(book1)
        self.library.add_book(book2)
        self.library.borrow_book(book1.isbn)
        self.library.borrow_book(book2.isbn)
        available_books = self.library.get_available_books()
        self.assertEqual(available_books, [])
    
    def test_search_for_available_books_only(self):
        book1 = Book(isbn='1234567890', title='Test-Driven', author='xyz', year=2002)
        self.library.add_book(book1) 
        results = self.library.search_books(title='Test-Driven')
        self.assertEqual(len(results), 1)
        self.assertEqual(results[0].title, 'Test-Driven')

    def test_borrow_and_return_multiple_books(self):
        book1 = Book(isbn="1234567890", title="Test-Driven", author="dhruv", year=1925)
        book2 = Book(isbn="0987654321", title="M.S Dhoni", author="maitri", year=1960)
        book3 = Book(isbn="1122334455", title="harray poter", author="dhruv", year=1949)
        
        self.library.add_book(book1)
        self.library.add_book(book2)
        self.library.add_book(book3)
        
        self.library.borrow_book("1234567890")
        self.library.borrow_book("0987654321")
        
        available = self.library.get_available_books()
        self.assertEqual(len(available), 1)
        self.assertEqual(available[0].isbn, "1122334455")
        
        self.library.return_book("1234567890")
        
        available = self.library.get_available_books()
        self.assertEqual(len(available), 2)
        isbns_available = [book.isbn for book in available]
        self.assertIn("1234567890", isbns_available)
        self.assertIn("1122334455", isbns_available)


if __name__ == '__main__':
    unittest.main()
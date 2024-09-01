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

    def test_duplicaterror(self):
        library = Library()
        book1 = {
            'isbn': '1234567890',
            'title': 'Test',
            'author': 'xyz',
            'year': 2002,
        }
        book2 = {
            'isbn': '1234567890',
            'title': 'python',
            'author': 'xyz',
            'year': 2002,
        }
        library.add_book(book1)
        try:
            library.add_book(book2) 
        except ValueError as e:  
            print("Caught an error: {e}")
        
            
        self.assertEqual(len(library.books), 2)
        self.assertEqual(library.books[0]['isbn'], '1234567890')

    def test_borrow_book(self):
        book = Book(isbn="1234567890", title="The Guide", author="RK Narayan", year=1958)
        self.library.add_book(book)
        self.library.borrow_book(book.isbn)
        self.assertTrue(book.is_borrowed)
    

if __name__ == '__main__':
    unittest.main()

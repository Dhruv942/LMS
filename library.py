class Book:
    def __init__(self, isbn, title, author, year):
        self.isbn = isbn
        self.title = title
        self.author = author
        self.year = year
        self.is_borrowed = False

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        if not book.author:
            raise ValueError("Book author cannot be empty")
        if book in self.books:
           raise ValueError("Book already in the library.")
        self.books.append(book)
    
    def borrow_book(self, isbn):
        for book in self.books:
            if book.isbn == isbn:
                if book.is_borrowed:
                    raise ValueError("Book is already borrowed.")
                book.is_borrowed = True
                return
        raise ValueError("Book not found in the library.")
    
    def return_book(self, isbn):
        for book in self.books:
            if book.isbn == isbn:
                if not book.is_borrowed:
                    raise ValueError("Book is not borrowed.")
                book.is_borrowed = False
                return
        raise ValueError("Book not found in the library.")
    

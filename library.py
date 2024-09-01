class Book:
    def __init__(self, isbn, title, author, year):
        self.isbn = isbn
        self.title = title
        self.author = author
        self.year = year

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        if book in self.books:
           raise ValueError("A book with this ISBN already in the library.")
        self.books.append(book)


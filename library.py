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
        
        self.books.append(book)


class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.page = 0

    def turn_page(self, page):
        self.page = page

    def __str__(self):
        return f'Book: {self.title} writen from {self.author}'


class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        for b in self.books:
            if b.title == book.title:
                return f'{book.title} is in the Library cannot add it'
        self.books.append(book)

    def find_book(self, title):
        return [b.title for b in self.books if b.title == title]


book1 = Book('Programming with Python', 'Svetlin Nakov')
book2 = Book('Programming with C#', 'Svetlin Nakov')
book2.turn_page(350)
print(book1)
print(book2)
library = Library()
library.add_book(book1)
library.add_book(book2)
print(library.find_book('Programming with Python'))
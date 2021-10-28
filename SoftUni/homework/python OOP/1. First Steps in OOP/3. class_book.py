class Book:

    def __init__(self, name, author, pages):
        self.name = name
        self.author = author
        self.pages = pages

book = Book("My Book", "Me", 200)
print(book.name)
print(book.author)
print(book.pages)
print("---------")
book_2 = Book('Lego', 'You', 100)
print(book_2.name)
print(book_2.author)
print(book_2.pages)
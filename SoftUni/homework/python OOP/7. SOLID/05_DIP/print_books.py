from abc import abstractmethod, ABC


class Book:
    def __init__(self, content: str, pages=100):
        self.content = content
        self.pages = pages


class BaseFormatter(ABC):
    @abstractmethod
    def format(self, book: Book):
        pass


class MobileFormatter(BaseFormatter):
    def format(self, book: Book) -> str:
        return book.content


class DesktopFormatter(BaseFormatter):
    def format(self, book: Book):
        return book.content[:100]


class Printer:
    def get_book(self, book: Book, formatter):
        print('Print...')
        return formatter.format(book)


printer = Printer()
book = Book('Hello World! ASDASDaDS')
formatter = MobileFormatter()
desktop_formatter = DesktopFormatter()
print(printer.get_book(book, formatter))
print(printer.get_book(book, desktop_formatter))
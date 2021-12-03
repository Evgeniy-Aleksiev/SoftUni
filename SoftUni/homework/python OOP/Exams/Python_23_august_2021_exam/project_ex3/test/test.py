from unittest import TestCase, main
from project.library import Library


class LibraryTest(TestCase):
    def setUp(self) -> None:
        self.library = Library('Gosho')

    def test_init_creates_all_attributes(self):
        self.assertEqual('Gosho', self.library.name)
        self.assertEqual({}, self.library.books_by_authors)
        self.assertEqual({}, self.library.readers)

    def test_name_empty_string(self):
        with self.assertRaises(ValueError) as ex:
            library = Library('')

        expected_result = "Name cannot be empty string!"
        self.assertEqual(expected_result, str(ex.exception))

    def test_add_book(self):
        self.library.add_book('Gosho', 'Title1')
        self.library.add_book('Gosho', 'Title2')

        self.assertEqual(1, len(self.library.books_by_authors))
        self.assertTrue('Gosho', self.library.books_by_authors)
        self.assertEqual(['Title1', 'Title2'], self.library.books_by_authors['Gosho'])

    def test_add_readers(self):
        self.library.add_reader('Pesho')

        self.assertEqual(1, len(self.library.readers))
        self.assertTrue('Pesho' in self.library.readers)
        self.assertEqual([], self.library.readers['Pesho'])

    def test_add_readers_should_throw_an_error(self):
        self.library.add_reader('Pesho')
        result = self.library.add_reader('Pesho')
        expected_result = f"Pesho is already registered in the {self.library.name} library."

        self.assertEqual(expected_result, result)

    def test_rent_book_reader_name_not_in_readers(self):
        reader_name = 'Pesho'
        book_author = 'Goshka'
        book_title = 'Title'
        result = self.library.rent_book(reader_name, book_author, book_title)
        expected_result = f"{reader_name} is not registered in the {self.library.name} Library."

        self.assertEqual(expected_result, result)

    def test_rent_book_author_not_in_library(self):
        reader_name = 'Pesho'
        book_author = 'Goshka'
        book_title = 'Title'
        self.library.add_reader(reader_name)

        result = self.library.rent_book(reader_name, book_author, book_title)
        expected_result = f"{self.library.name} Library does not have any {book_author}'s books."

        self.assertEqual(expected_result, result)

    def test_rent_book_title_not_in_library(self):
        reader_name = 'Pesho'
        book_author = 'Goshka'
        book_title = 'Title'
        self.library.add_reader(reader_name)
        self.library.add_book(book_author, 'Title1')

        result = self.library.rent_book(reader_name, book_author, book_title)
        expected_result = f"""{self.library.name} Library does not have {book_author}'s "{book_title}"."""
        self.assertEqual(expected_result, result)

    def test_rent_book(self):
        reader_name = 'Pesho'
        book_author = 'Goshka'
        book_title = 'Title'
        book_title2 = 'Title2'

        self.library.add_reader(reader_name)
        self.library.add_book(book_author, book_title)
        self.library.add_book(book_author, book_title2)
        self.library.rent_book(reader_name, book_author, book_title)

        self.assertEqual([{book_author: book_title}], self.library.readers[reader_name])
        self.assertEqual(1, len(self.library.books_by_authors[book_author]))
        self.assertTrue(book_title not in self.library.books_by_authors[book_author])
        self.assertTrue(book_title2 in self.library.books_by_authors[book_author])


if __name__ == '__main__':
    main()

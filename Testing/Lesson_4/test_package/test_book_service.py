import unittest
from unittest import mock

from Testing.Lesson_4.hw4.book import Book
from Testing.Lesson_4.hw4.book_repository import BookRepository
from Testing.Lesson_4.hw4.book_service import BookService


class TestServiceBook(unittest.TestCase):

    def setUp(self):
        # Создаем мок-объект для зависимости
        self.repo_mock = mock.MagicMock(spec=BookRepository, name='book_mock_repo')
        self.book_service = BookService(self.repo_mock)

    def tearDown(self):
        self.repo_mock = None
        self.book_service = None

    def test_find_book_by_id(self):
        book_id: str = '1'
        expected_book: Book = Book(book_id, 'Book 1', 'Author 1')
        self.repo_mock.find_book_by_id.return_value = expected_book
        result_book: Book = self.book_service.find_book_by_id(book_id)
        # проверить, что метод был вызван с правильными аргументами
        self.repo_mock.find_book_by_id.assert_called_with('1')
        self.assertEqual(result_book, expected_book)

    def test_find_all_books(self):
        expected_books = [
            Book("1", "Book1", "Author1"),
            Book("2", "Book2", "Author2"),
        ]
        self.repo_mock.find_all_books.return_value = expected_books
        result_books: list[Book] = self.book_service.find_all_books()
        self.repo_mock.find_all_books.assert_called_with()
        self.assertEqual(expected_books, result_books)


if __name__ == "__main__":
    unittest.main()

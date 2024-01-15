from Testing.Lesson_4.hw4.book import Book
from Testing.Lesson_4.hw4.book_repository import BookRepository


class BookService:

    def __init__(self, book_repository: BookRepository):
        self._book_repository = book_repository

    def find_book_by_id(self, book_id: str) -> Book:
        return self._book_repository.find_book_by_id(book_id)

    def find_all_books(self) -> list[Book]:
        return self._book_repository.find_all_books()

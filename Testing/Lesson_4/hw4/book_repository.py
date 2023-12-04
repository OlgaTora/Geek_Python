from abc import ABC, abstractmethod

from Testing.Lesson_4.hw4.book import Book


class BookRepository(ABC):
    @abstractmethod
    def find_book_by_id(self, book_id: str) -> Book:
        pass

    @abstractmethod
    def find_all_books(self) -> list[Book]:
        pass

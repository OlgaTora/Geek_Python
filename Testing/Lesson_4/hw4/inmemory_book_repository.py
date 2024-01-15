from Testing.Lesson_4.hw4.book import Book
from Testing.Lesson_4.hw4.book_repository import BookRepository


class InMemoryBookRepository(BookRepository):

    def __init__(self):
        self.books = [Book("1", "Book1", "Author1"), Book("2", "Book2", "Author2")]

    def find_book_by_id(self, book_id: str) -> Book:
        for book in self.books:
            if book.book_id == book_id:
                return book

    def find_all_books(self) -> list[Book]:
        return self.books

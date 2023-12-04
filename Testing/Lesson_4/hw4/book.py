class Book:
    def __init__(self, book_id: str, title: str = None, author: str = None):
        self.book_id = book_id
        self.title = title
        self.author = author

    def get_book_id(self) -> str:
        return self.book_id

    def set_book_id(self, book_id: str):
        self.book_id = book_id

    def get_title(self) -> str:
        return self.title

    def set_title(self, title: str):
        self.title = title

    def get_author(self) -> str:
        return self.author

    def set_author(self, author: str):
        self.author = author

from Package02.BookNotFoundError import BookNotFoundError


class Library:

    def __init__(self):
        self.books = list()

    def add_book(self, title: str):
        self.books.append(title)

    def remove_books(self, title: str):
        if title in self.books:
            self.books.remove(title)
        else:
            raise BookNotFoundError

    def list_books(self) -> list[str]:
        return self.books

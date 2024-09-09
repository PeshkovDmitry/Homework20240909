class BookNotFoundError(Exception):

    def __init__(self):
        super().__init__("Книга не найдена")



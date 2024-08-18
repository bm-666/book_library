from library.models import Book

class BookStruct:
    id: int
    name: str
    author: str
    genre: str

    def __init__(self, data: Book) -> None:
        self.id = data.id
        self.name = data.name
        self.author = data.author.name
        self.genre = data.genre.name

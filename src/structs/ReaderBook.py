from datetime import datetime
from library.models import ReaderBook

class ReaderBookStruct:
    id: int
    name: str # название книги
    date_get: datetime # дата получения книги
    days_on_hands: int # количество дней на руках

    def __init__(self, data: ReaderBook) -> None:
        self.id = data.id
        self.name = data.book.name
        self.date_get = data.date_took
        self.days_on_hands = data.days_user_book
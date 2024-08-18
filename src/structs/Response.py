from enums.ResponseStatus import ResponseStatus
from typing import Any

class BaseResponse:
    results: Any

    def __init__(self, data: Any):
        self.results = data

class BookResponseStruct:
    book: int # id книги
    status: ResponseStatus # статус ответа

    def __init__(self, id: int, status: ResponseStatus) -> None:
        self.book = id
        self.status = status

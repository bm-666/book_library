from enum import StrEnum


class BookStatus(StrEnum):
    AVAILABLE = 'available'
    BUSY = 'busy'
    NOT_AVAILABLE = 'not_available'

from enums.BookStatus import BookStatus
from enums.Role import Role

BOOK_STATUS = (
    (BookStatus.AVAILABLE, 'доступен'),
    (BookStatus.BUSY, 'занят'),
    (BookStatus.NOT_AVAILABLE, 'не доступен')
)


ROLE = (
    (Role.LIBRARIAN, Role.LIBRARIAN),
    (Role.READER, Role.READER)
)
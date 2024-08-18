from datetime import datetime
import logging

from django.core.exceptions import ObjectDoesNotExist

from enums.BookStatus import BookStatus
from enums.ResponseStatus import ResponseStatus
from library.models import Book, ReaderBook
from structs.Response import BookResponseStruct

logger = logging.getLogger(__name__)


def func_return_book(book_id: int, reader_id: int) -> BookResponseStruct:
    """функция вернуть книгу
    :param book_id id книги
    :param reader_id id пользователя от которого пришел запрос
    """
    try:
        status = Book.objects.get(id=book_id).status
        if  status == BookStatus.BUSY:
            debt = ReaderBook.objects.get(reader_id=reader_id, book_id=book_id, date_return=None)

            ReaderBook.objects.filter(id=debt.id).update(date_return=datetime.now())
            Book.objects.filter(id=book_id).update(status=BookStatus.AVAILABLE)

            return BookResponseStruct(id=book_id, status=ResponseStatus.SUCCESS)

        elif status == BookStatus.AVAILABLE:
            return BookResponseStruct(id=book_id, status=ResponseStatus.COMMAND_NOT_AVAILABLE)

        else:
            #TODO Здесь должна быть логика под други варианты статусов
            return BookResponseStruct(id=book_id, status=ResponseStatus.COMMAND_NOT_AVAILABLE)

    except Exception as e:
        logger.exception(e)
        pass


def func_get_book(book_id: int, reader_id: int) -> dict:
    """ метод взять книгу
        :param book_id id книги
        :param reader_id id пользователя от которого пришел запрос
        """
    try:
        book = Book.objects.get(id=book_id)
        if book.status == BookStatus.AVAILABLE:
            ReaderBook.objects.create(reader_id=reader_id, book_id=book_id)
            Book.objects.update(status=BookStatus.BUSY)
            return {'book': book_id, 'status': ResponseStatus.SUCCESS}
        else:
            return {'book': book_id, 'status': BookStatus.BUSY}
    except ObjectDoesNotExist:
        return {'book': book_id, 'status': ResponseStatus.DOES_NOT_EXIST}

    except Exception as e:
        logger.exception(e)
        raise



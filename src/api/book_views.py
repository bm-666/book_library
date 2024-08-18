import logging

from drf_spectacular.utils import extend_schema
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework import status
from rest_framework_simplejwt.authentication import JWTAuthentication

from auth_users.views.auth import user_logout
from library.models import Book
from library.models import ReaderBook

from structs.Book import BookStruct
from enums.Role import Role
from enums.ResponseStatus import ResponseStatus
from structs.Response import BaseResponse, BookResponseStruct
from structs.ReaderBook import ReaderBookStruct
from .service import func_return_book, func_get_book
from .serializer.BookSerializer import BookGetSerializer, BooksSerializer
logger = logging.getLogger(__name__)


@extend_schema(responses=BooksSerializer, summary='получить список книг')
@api_view(['GET'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def show_list_books(request: Request) -> Response:
    """получение списка книг"""
    try:
        books: list[dict] = [BookStruct(book).__dict__ for book in Book.objects.all()]
        return Response(status=status.HTTP_200_OK, data={'results': books})
    except Exception as e:
        logger.exception(e)
        raise


@extend_schema(responses=BookGetSerializer, summary='взять книгу')
@api_view(['GET'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def get_book(request: Request, id: int) -> Response:
    """
    получение книги
    :param book id книги
    ответ статус выполнения команды
    """
    try:

        if not isinstance(id, int):
            return Response(status=status.HTTP_400_BAD_REQUEST, data={'book':id, 'status': ResponseStatus.INCORRECT_PARAMETER})

        if request.user.role == Role.READER:
            data = func_get_book(book_id=id, reader_id=request.user.id)
            return Response(status=status.HTTP_200_OK, data=data)

        else:
            return Response(status=status.HTTP_403_FORBIDDEN, data={'book': id, 'status': ResponseStatus.FORBIDDEN})

    except Exception as e:
        logger.exception(e)
        raise

@extend_schema(responses=BookGetSerializer, summary='вернуть книгу')
@api_view(['GET'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def return_book(request: Request, id :int) -> Response:
    """метод возврат книги

    :param book id возвращаемой  книги
    ответ статус выполнения команды
    """

    try:
        if not isinstance(id, int):
            return Response(
                status=status.HTTP_400_BAD_REQUEST,
                data=BookResponseStruct(id=id, status = ResponseStatus.INCORRECT_PARAMETER).__dict__
                )

        if request.user.role == Role.READER:
            data = func_return_book(book_id=id, reader_id=request.user.id)
            return Response(status=status.HTTP_200_OK, data=data.__dict__)

        else:
            return Response(
                status=status.HTTP_403_FORBIDDEN,
                data=BookResponseStruct(id=id, status=ResponseStatus.FORBIDDEN).__dict__
            )
    except Exception as e:
        logger.exception(e)
        raise

@extend_schema(responses=BooksSerializer, summary='получить список книг на руках')
@api_view(['GET'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def get_reader_book(request: Request) -> Response:
    """метод получение всех книг которые сейчас у читателей"""
    try:
        books: list[dict] = [ReaderBookStruct(item).__dict__
                             for item in  ReaderBook.objects.filter(date_return=None).order_by('-book')]

        return Response(status=status.HTTP_200_OK, data=BaseResponse(books).__dict__)
    except Exception as e:
        logger.exception(e)
        raise
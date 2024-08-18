from datetime import datetime
import logging
from django.forms.forms import Form
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_list_or_404

from django.http.request import HttpRequest
from django.http.response import HttpResponse
from django.contrib.auth.decorators import login_required

from ..models import Book, CustomUser,Reader, ReaderBook
from enums.BookStatus import BookStatus

logger = logging.getLogger(__name__)


#@login_required()
def index(request):
    """отображение главной страници по ролям"""
    if request.user.is_anonymous or request.user.role == 'reader':
        books = get_list_or_404(Book.objects.order_by('name'))
        return render(request, 'book/books.html', context={'books': books})

    elif request.user.role == 'librarian':
        debtors = get_list_or_404(ReaderBook, date_return=None)
        return render(request, 'book/debtors.html', context={'debtors': debtors})
    elif request.user.is_superuser:
       return HttpResponseRedirect('/admin')


@login_required()
def get_book(request):
    """метод взять книгу"""
    if request.method != 'POST':
        return render(request, '', context={})
    form = Form(request.POST)

    if form.is_valid():
        user_id = request.user.id
        book_id = int(form.data.get('btn'))
        ReaderBook.objects.create(reader_id=user_id, book_id=book_id)
        Book.objects.filter(id=book_id).update(status=BookStatus.BUSY)

        return HttpResponseRedirect('/')
@login_required()
def get_user_books(request: HttpRequest, id: int) -> list[ReaderBook] | HttpResponse:
    """отображение всех книг которые взял читатель

    param: id reader id
    """
    user_books = get_list_or_404(ReaderBook, reader_id=id, date_return=None)

    return render(request, 'book/user_books.html', context={'user_books': user_books})

@login_required()
def return_book(request):
    """ возврат книги"""
    try:
        if request.method != 'POST':
            return render(request, '', context={})
        form = Form(request.POST)

        if form.is_valid():
            user_id = request.user.id
            book_id = int(form.data.get('btn'))
            ReaderBook.objects.filter(reader_id=user_id, book_id=book_id).update(date_return=datetime.now())
            Book.objects.filter(id=book_id).update(status=BookStatus.AVAILABLE)

            return HttpResponseRedirect('/')
    except Exception as e:
        logger.exception(e)

from django.urls import path
from . import book_views

urlpatterns = [
    path('books', book_views.show_list_books),
    path('book/get_book/<int:id>', book_views.get_book),
    path('book/return_book/<int:id>', book_views.return_book),
    path('book/reader_book', book_views.get_reader_book)
]
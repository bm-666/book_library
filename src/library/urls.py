from django.urls import path
from .views import book_views
from .views.LibraryView import HomePageView
from .views.auth import auth_page


urlpatterns = [
    path('', book_views.index),
    path('auth_page/', auth_page),
    path('reader/get_book', book_views.get_book),
    path('reader/return_book', book_views.return_book),
    path('reader/<int:id>/books', book_views.get_user_books),
]
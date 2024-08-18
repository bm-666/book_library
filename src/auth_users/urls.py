from django.urls import path
from .views import auth

urlpatterns = [
    path('sign_in', auth.sign_in),
    path('librarian', auth.sign_out),
    path('reader', auth.sign_out),
    path('logout', auth.user_logout)
    #path('reader'),
]
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from simple_history.models import HistoricalRecords

from auth_users.forms import CustomCreateUserForm
from django.contrib.auth.models import User
from simple_history.admin import SimpleHistoryAdmin

from .models import (
    Author,
    Book,
    CustomUser,
    Genre,
    ReaderBook,

)

@admin.register(CustomUser)
class CustomerUserAdmin(UserAdmin):
    add_form = CustomCreateUserForm
    list_display = ('username', 'employee_id' )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email','password1', 'password2','role', 'first_name',  'last_name', 'address','employee_id'),
        }),
    )


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    ...


@admin.register(Book)
class BookAdmin(SimpleHistoryAdmin):
    list_display = ['name', 'author', 'genre', 'status']


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    ...


@admin.register(ReaderBook)
class ReaderBookModelAdmin(admin.ModelAdmin):
    #fields = ('reader', 'book', 'date_took', 'date_return')
    list_display = ['reader', 'book', 'date_took', 'date_return']
    list_filter = ['date_return']












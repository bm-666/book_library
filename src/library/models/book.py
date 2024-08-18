from django.db import models
from .choices import BOOK_STATUS
from simple_history.models import HistoricalRecords

class Book(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=1000)
    genre = models.ForeignKey('Genre', on_delete=models.SET_NULL, null=True, blank=True, default='')
    author = models.ForeignKey('Author', on_delete=models.SET_NULL, null=True)
    status = models.CharField(choices=BOOK_STATUS, max_length=20)
    description = models.TextField(max_length=10000, null=True, blank=True)
    history = HistoricalRecords()
    class Meta:
        db_table = 'books'
        verbose_name = 'Книга'
        verbose_name_plural = 'Книги'

    def __str__(self):
        return self.name


class Genre(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        db_table = 'genres'
        verbose_name = 'Жанр'
        verbose_name_plural = 'Жанры'
    def __str__(self):
        return self.name

class Author(models.Model):
    name = models.CharField(max_length=500)

    class Meta:
        db_table = 'author'

        verbose_name = 'Автор'
        verbose_name_plural = 'Авторы'


    def __str__(self):
        return self.name

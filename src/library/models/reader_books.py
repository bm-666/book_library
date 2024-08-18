from datetime import timedelta, date

from django.db import models
from django.utils import timezone
from simple_history.models import HistoricalRecords

from . import Book, CustomUser

class ReaderBook(models.Model):
    id = models.AutoField(primary_key=True)
    reader = models.ForeignKey(CustomUser, on_delete=models.PROTECT, null=True)
    book = models.ForeignKey(Book, on_delete=models.PROTECT, null=True)
    date_took = models.DateTimeField(default=timezone.now)
    date_return = models.DateTimeField(null=True, blank=True)
    history = HistoricalRecords()

    class Meta:
        db_table = 'reader_book'
        verbose_name = 'Должник'
        verbose_name_plural = 'Должники'

    def __str__(self):
        return self.reader.username

    @property
    def days_user_book(self):
        """ определяем сколько дней книга у читателя"""
        return (timezone.now() - self.date_took).days




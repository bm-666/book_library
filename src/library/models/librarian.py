from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from . import BasePerson
class Librarian(BasePerson):

    employee_id = models.CharField(max_length=50, unique=True)

    class Meta:
        db_table = 'librarian'
        verbose_name = 'Библиотекарь'
        verbose_name_plural ='Библиотекари'

    def __str__(self):
        return self.username

"""@receiver(post_save, sender=User)
def create_user_librarian(sender, instance, created, **kwargs):
    if created:
        Librarian.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_librarian(sender, instance, **kwargs):
    instance.librarian.save()
"""
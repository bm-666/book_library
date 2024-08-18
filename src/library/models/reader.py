from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from . import BasePerson

class Reader(BasePerson):
    address = models.TextField()


    class Meta:
        db_table = 'reader'
        verbose_name = 'Читатель'
        verbose_name_plural = 'Читатели'

    def __str__(self):
        return self.username


"""@receiver(post_save, sender=User)
def create_user_librarian(sender, instance, created, **kwargs):
    if created:
        Reader.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_librarian(sender, instance, **kwargs):
    instance.reader.save()
"""
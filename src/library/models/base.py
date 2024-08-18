import uuid
from django.db import models
from django.template.base import kwarg_re

from . import Author
from .choices import ROLE
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import Group

class BasePerson(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    username = models.CharField(max_length=50, unique=True)
    password = models.CharField(max_length=1000)
    email = models.EmailField(unique=True)


    def save(self, *args, **kwargs):
        #self.set_password(self.password)
        super().save(*args, **kwargs)

    def set_password(self, raw_password):
        self.password = make_password(raw_password)

class CustomUser(AbstractUser):
    password = models.CharField(max_length=128)
    address = models.CharField(max_length=120, null=True, blank=True)
    employee_id = models.CharField(max_length=50, unique=True, blank=True, null=True)
    role = models.CharField(choices=ROLE, max_length=100, null=True, blank=True)

    #is_staff = models.BooleanField()
    class Meta:

        db_table = 'customer_user'
        verbose_name = 'пользователи'
    def __str__(self):
        return self.username

@receiver(post_save, sender=CustomUser)
def user(sender: CustomUser, instance: CustomUser, created: bool, **kwargs) -> None:
    if created:
        print('123412124124')
        print('role -----> ', instance.role)
        if instance.role  is not None:

            group = Group.objects.get(name=instance.role)
            instance.groups.add(group)
    """else:
        group = Group.objects.get(name=instance.role)
        instance.groups.add(group)
"""
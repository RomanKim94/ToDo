from django.contrib.auth.models import AbstractUser, User
from django.db import models


class Person(AbstractUser):
    birth_date = models.DateField(
        verbose_name='Дата рождения',
        blank=True,
    )

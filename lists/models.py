from django.db import models


class List(models.Model):
    name = models.CharField(
        verbose_name='Название списка',
        max_length=40,
    )
    person = models.ForeignKey(
        'persons.Person',
        verbose_name='Пользователь',
        on_delete=models.CASCADE,
        related_name='Lists',
    )

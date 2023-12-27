import datetime

from django.db import models


class Task(models.Model):
    STAGES = (
        ('done', 'DONE'),
        ('not_done', 'NOT DONE'),
        ('processing', 'PROCESSING'),
        ('canceled', 'CANCELED'),
    )

    name = models.CharField(
        verbose_name='Название задачи',
        max_length=200,
    )
    description = models.TextField(
        verbose_name='Описание задачи',
        blank=True,
    )
    is_done = models.CharField(
        verbose_name='Этап выполнения задачи',
        max_length=10,
        choices=STAGES,
    )
    deadline = models.DateTimeField(
        verbose_name='Срок выполнения задачи',
        blank=True,
    )
    create_time = models.DateTimeField(
        verbose_name='Время создания задачи',
        blank=True,
        auto_now_add=True,
    )
    update_time = models.DateTimeField(
        verbose_name='Время последнего изменения задачи',
        blank=True,
        auto_now=True,
    )
    list = models.ForeignKey(
        'lists.List',
        verbose_name='Список задач',
        blank=True,
        on_delete=models.CASCADE,
        related_name='Tasks'
    )

import datetime

from django.db import models


class Task(models.Model):
    STAGES = (
        ('done', 'DONE'),
        ('not_done', 'NOT DONE'),
        ('processing', 'PROCESSING'),
        ('canceled', 'CANCELED'),
    )
    PRIORITY = (
        ('1', 'Высший'),
        ('2', 'Средний'),
        ('3', 'Низкий'),
        ('4', 'Без приоритета'),
    )

    name = models.CharField(
        verbose_name='Название задачи',
        max_length=200,
    )
    description = models.TextField(
        verbose_name='Описание задачи',
        blank=True,
    )
    stage = models.CharField(
        verbose_name='Этап выполнения задачи',
        max_length=10,
        choices=STAGES,
        blank=True,
        default='not_done',
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
        related_name='Tasks',
    )
    priority = models.IntegerField(
        verbose_name='Уровень приоритета',
        choices=PRIORITY,
        blank=True,
        default='1',
    )

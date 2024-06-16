from django.db import models
from django.contrib.auth import get_user_model

from cafes.models.departments import Department

User = get_user_model()


class Position(models.Model):
    """Должности"""
    name = models.CharField('Название должности', max_length=64)
    department = models.ForeignKey(Department, on_delete=models.CASCADE,
                                   verbose_name='Отдел')

    class Meta:
        verbose_name = 'Должность'
        verbose_name_plural = 'Должности'
        ordering = ('name',)

    def __str__(self):
        return f'{self.name} ({self.id})'

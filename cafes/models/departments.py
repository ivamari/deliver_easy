from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Department(models.Model):
    """Отделы"""
    name = models.CharField('Название отдела', max_length=64)
    description = models.TextField('Описание отдела')

    class Meta:
        verbose_name = 'Отдел'
        verbose_name_plural = 'Отделы'

    def __str__(self):
        return f'{self.name} ({self.pk})'

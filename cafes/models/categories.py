from django.db import models

from common.models.mixins import BaseDictModelMixin


class Category(BaseDictModelMixin):
    """Категории"""
    cooking_time = models.IntegerField('Время приготовления(мин)')

    class Meta:
        verbose_name = 'Категория товаров'
        verbose_name_plural = 'Категории товаров'

    def __str__(self):
        return f'{self.name} ({self.pk})'

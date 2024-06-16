from django.db import models

from common.models.mixins import BaseDictModelMixin


class Category(BaseDictModelMixin):
    """Категории"""

    class Meta:
        verbose_name = 'Категория товаров'
        verbose_name_plural = 'Категории товаров'

    def __str__(self):
        return self.name


class CategoryCookingTime(models.Model):
    """Время приготовления категорий"""
    category = models.OneToOneField(Category,
                                    on_delete=models.CASCADE,
                                    verbose_name='Категория')
    cooking_time = models.IntegerField('Время приготовления(мин)',
                                       null=True, blank=True)

    class Meta:
        verbose_name = 'Время приготовления категории'
        verbose_name_plural = 'Время приготовления категорий'

    def __str__(self):
        return f'{self.category} - {self.cooking_time}'

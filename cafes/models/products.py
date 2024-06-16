from django.db import models

from cafes.models.cafes import Cafe
from cafes.models.categories import Category


class Product(models.Model):
    """Продукты"""
    name = models.CharField('Название', max_length=20)
    price = models.IntegerField('Стоимость')
    category = models.ForeignKey(Category,
                                 models.RESTRICT,
                                 'category_products',
                                 verbose_name='Категория')
    cafe = models.ManyToManyField(Cafe, verbose_name='Кафе', blank=True)

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'

    def __str__(self):
        return f'{self.name} ({self.pk})'

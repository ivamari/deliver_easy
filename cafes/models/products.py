from django.db import models

from cafes.models.cafes import Cafe
from cafes.models.categories import Category


class Product(models.Model):
    name = models.CharField('Название', max_length=20)
    price = models.IntegerField('Стоимость')
    category = models.ForeignKey(Category,
                                 models.RESTRICT,
                                 'category_products',
                                 verbose_name='Категория')
    cafe = models.ManyToManyField(Cafe, verbose_name='Кафе', null=True, blank=True)

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'

    def __str__(self):
        return self.name


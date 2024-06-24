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
    cafe = models.ManyToManyField(Cafe, verbose_name='Кафе',
                                  through='CafeProduct'
                                  )

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'

    def __str__(self):
        return f'{self.name} ({self.pk})'


class CafeProduct(models.Model):
    """Кафе/продукты"""
    cafe = models.ForeignKey(Cafe, on_delete=models.CASCADE,
                             related_name='products_cafe',
                             verbose_name='Кафе')
    product = models.ForeignKey(Product, on_delete=models.CASCADE,
                                related_name='cafe_products',
                                verbose_name='Продукты')

    class Meta:
        verbose_name = 'Товары кафе'
        verbose_name_plural = 'Товары кафе'

    def __str__(self):
        return f'{self.cafe} - {self.product}'

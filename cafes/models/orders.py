from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.gis.db import models as geo_models

from cafes.models.products import Product
from common.models.mixins import BaseDictModelMixin

User = get_user_model()


class OrderStatus(BaseDictModelMixin):
    class Meta:
        verbose_name = 'Статус заказа'
        verbose_name_plural = 'Статусы заказов'


class Order(models.Model):
    user = models.ManyToManyField(User,
                                  verbose_name='Пользователь'
                                  )
    location = geo_models.PointField('Локация')
    status = models.ForeignKey(OrderStatus,
                               models.RESTRICT,
                               'status_orders',
                               verbose_name='Статусы')
    order_date = models.DateField('Дата заказа', auto_now_add=True)
    order_time = models.TimeField('Время заказа', auto_now_add=True)
    cooking_time = models.IntegerField('Время приготовления заказа',
                                       null=True, blank=True)
    delivery_time = models.IntegerField('Длительность доставки',
                                        null=True,
                                        blank=True)
    order_price = models.IntegerField('Стоимость заказа',
                                      null=True, blank=True)
    total_price = models.IntegerField('Сумма заказ + доставка', blank=True,
                                      null=True)

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'

    def __str__(self):
        return f'Корзина {self.user}'


class OrderProduct(models.Model):
    order = models.ForeignKey(Order, models.CASCADE,
                              'order_products',
                              verbose_name='Заказ')
    product = models.ForeignKey(Product, models.CASCADE,
                                'product_orders')
    amount = models.IntegerField('Количество')

    class Meta:
        verbose_name = 'Продукт заказа'
        verbose_name_plural = 'Продукты заказов'

    def __str__(self):
        return f'{self.order} - {self.product}'

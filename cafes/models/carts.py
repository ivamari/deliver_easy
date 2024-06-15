from django.db import models

from cafes.models.products import Product
from django.contrib.auth import get_user_model

User = get_user_model()


class Cart(models.Model):
    """Корзина пользователя"""
    user = models.OneToOneField(User,
                                on_delete=models.CASCADE,
                                related_name='user_cart')
    products = models.ManyToManyField(Product,
                                      through='CartProduct',
                                      verbose_name='Продукты')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Корзина'
        verbose_name_plural = 'Корзины'

    def __str__(self):
        return f'Корзина {self.user}'


class CartProduct(models.Model):
    """Промежуточная модель корзины/продуктов"""
    cart = models.ForeignKey(Cart, models.CASCADE,
                             'cart_products',
                             verbose_name='Корзина пользователя')
    product = models.ForeignKey(Product, models.CASCADE,
                                'product_carts',
                                verbose_name='Продукт')
    amount = models.IntegerField('Количество')

    class Meta:
        verbose_name = 'Корзина с продуктами'
        verbose_name_plural = 'Корзины с продуктами'

    def __str__(self):
        return f'{self.cart} - {self.product}'

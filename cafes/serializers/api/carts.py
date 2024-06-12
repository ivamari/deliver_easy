from django.contrib.auth import get_user_model
from rest_framework import serializers

from cafes.models.carts import Cart
from cafes.models.categories import CategoryCookingTime
from cafes.serializers.nested.products import ProductShortSerializer
from common.serializers.mixins import ExtendedModelSerializer

User = get_user_model()


########################
# CARTS
########################

class CartRetrieveSerializer(ExtendedModelSerializer):
    """Сериализатор для получения корзины пользователя по id пользователя"""

    products = ProductShortSerializer(many=True)

    class Meta:
        model = Cart
        fields = (
            'id',
            'user',
            'products',
            'created_at',
            'updated_at',
        )


class MeCartRetrieveSerializer(ExtendedModelSerializer):
    """Сериализатор для получения своей корзины пользователем"""

    products = ProductShortSerializer(many=True)

    class Meta:
        model = Cart
        fields = (
            'id',
            'products',
        )


# реализовать сериализатор для добавления товара в корзину пользователя
# реализовать сериализатор для удаления товара из корзины пользователя
# реализовать сериализатор для получения своей корзины пользователем


########################
# CATEGORY_COOKING_TIME
########################

class CategoryCookingTimeListSerializer(ExtendedModelSerializer):
    class Meta:
        model = CategoryCookingTime
        fields = (
            'id',
            'category',
            'cooking_time',
        )


class CategoryCookingTimeRetrieveSerializer(ExtendedModelSerializer):
    class Meta:
        model = CategoryCookingTime
        fields = (
            'id',
            'category',
            'cooking_time',
        )


class CategoryCookingTimeCreateSerializer(ExtendedModelSerializer):
    class Meta:
        model = CategoryCookingTime
        fields = (
            'id',
            'category',
            'cooking_time',
        )


class CategoryCookingTimeUpdateSerializer(ExtendedModelSerializer):
    class Meta:
        model = CategoryCookingTime
        fields = (
            'id',
            'category',
            'cooking_time',
        )


class CategoryCookingTimeDeleteSerializer(serializers.Serializer):
    pass

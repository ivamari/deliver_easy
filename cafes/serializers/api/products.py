from django.contrib.auth import get_user_model
from rest_framework import serializers

from cafes.models.products import Product
from cafes.serializers.nested.cafes import CafeShortSerializer
from cafes.serializers.nested.categories import CategoryShortSerializer
from common.serializers.mixins import ExtendedModelSerializer

User = get_user_model()


###############
# PRODUCT_CAFE
###############

class ProductCafeListSerializer(ExtendedModelSerializer):
    """Сериализатор для списка товаров отдельного кафе"""
    # cafe = CafeShortSerializer(many=True)
    category = CategoryShortSerializer()

    class Meta:
        model = Product
        fields = (
            'id',
            'name',
            'price',
            'available',
            'category',
            # 'cafe'
        )


class ProductCafeRetrieveSerializer(ExtendedModelSerializer):
    """Сериализатор для получения товара отдельного кафе"""
    cafe = CafeShortSerializer(many=True)
    category = CategoryShortSerializer()

    class Meta:
        model = Product
        fields = (
            'id',
            'name',
            'price',
            'available',
            'category',
            'cafe',
        )



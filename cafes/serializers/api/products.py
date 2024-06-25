from django.contrib.auth import get_user_model
from rest_framework import serializers
from rest_framework.exceptions import ParseError

from cafes.models.categories import Category
from cafes.models.products import Product
from cafes.serializers.nested.cafes import CafeShortSerializer
from cafes.serializers.nested.categories import CategoryShortSerializer

from common.serializers.mixins import ExtendedModelSerializer


User = get_user_model()


#################
# PRODUCT_CAFE
#################

class ProductCafeListSerializer(ExtendedModelSerializer):
    """Сериализатор для списка товаров отдельного кафе"""
    category = CategoryShortSerializer()

    class Meta:
        model = Product
        fields = (
            'id',
            'name',
            'price',
            'category',
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
            'category',
            'cafe',
        )


###############
# PRODUCT
###############

class ProductListSerializer(ExtendedModelSerializer):
    """Сериализатор для списка товаров"""
    cafe = CafeShortSerializer(many=True)
    category = CategoryShortSerializer()

    class Meta:
        model = Product
        fields = (
            'id',
            'name',
            'price',
            'category',
            'cafe'
        )


class ProductRetrieveSerializer(ExtendedModelSerializer):
    """Сериализатор для получения товара"""
    cafe = CafeShortSerializer(many=True)
    category = CategoryShortSerializer()

    class Meta:
        model = Product
        fields = (
            'id',
            'name',
            'price',
            'category',
            'cafe'
        )


class ProductCreateSerializer(ExtendedModelSerializer):
    """Сериализатор для создания товара"""
    category = serializers.PrimaryKeyRelatedField(
        queryset=Category.objects.all(),
        # source='category_products'
    )

    class Meta:
        model = Product
        fields = (
            'id',
            'name',
            'price',
            'category',
        )

    def validate_name(self, value):
        if self.Meta.model.objects.filter(name=value):
            raise ParseError(
                'Такой товар уже существует.'
            )
        return value


class ProductUpdateSerializer(ExtendedModelSerializer):
    """Сериализатор для обновления товара"""
    category = serializers.PrimaryKeyRelatedField(
        queryset=Category.objects.all())

    class Meta:
        model = Product
        fields = (
            'id',
            'name',
            'price',
            'category',
        )


class ProductDeleteSerializer(serializers.Serializer):
    """Сериализатор для удаления товара"""
    pass

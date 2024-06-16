from django.contrib.auth import get_user_model
from rest_framework.exceptions import ParseError

from cafes.models.products import Category
from common.serializers.mixins import ExtendedModelSerializer

User = get_user_model()


class CategoryListSerializer(ExtendedModelSerializer):
    """Сериализатор для списка категорий"""
    class Meta:
        model = Category
        fields = (
            'id',
            'name',
            'code',
            'cooking_time'
        )


class CategoryRetrieveSerializer(ExtendedModelSerializer):
    """Сериализатор для получения категории"""
    class Meta:
        model = Category
        fields = (
            'id',
            'name',
            'code',
            'cooking_time',
        )


class CategoryCreateSerializer(ExtendedModelSerializer):
    """Сериализатор для создания категории"""
    class Meta:
        model = Category
        fields = (
            'id',
            'name',
            'code',
            'cooking_time',
        )

    def validate_name(self, value):
        if self.Meta.model.objects.filter(name=value):
            raise ParseError(
                'Категория с таким названием уже существует.'
            )
        return value

    def validate_code(self, value):
        if self.Meta.model.objects.filter(code=value):
            raise ParseError(
                'Категория с таким кодом уже существует.'
            )
        return value

    def validate_cooking_time(self, value):
        if value <= 0:
            raise ParseError('Время приготовления не может быть отрицательным.')
        return value


class CategoryUpdateSerializer(ExtendedModelSerializer):
    """Сериализатор для обновления категории"""
    class Meta:
        model = Category
        fields = (
            'id',
            'name',
            'code',
            'cooking_time',
        )

    def validate_name(self, value):
        if self.Meta.model.objects.filter(name=value):
            raise ParseError(
                'Категория с таким названием уже существует.'
            )
        return value

    def validate_code(self, value):
        if self.Meta.model.objects.filter(code=value):
            raise ParseError(
                'Категория с таким кодом уже существует.'
            )
        return value

    def validate_cooking_time(self, value):
        if value <= 0:
            raise ParseError('Время приготовления не может быть отрицательным.')
        return value

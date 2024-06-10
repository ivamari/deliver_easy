from django.contrib.auth import get_user_model
from rest_framework import serializers

from cafes.models.categories import CategoryCookingTime
from cafes.models.products import Category
from common.serializers.mixins import ExtendedModelSerializer

User = get_user_model()

########################
# CATEGORY
########################


class CategoryListSerializer(ExtendedModelSerializer):
    class Meta:
        model = Category
        fields = (
            'id',
            'name',
            'code',
        )


class CategoryRetrieveSerializer(ExtendedModelSerializer):
    class Meta:
        model = Category
        fields = (
            'id',
            'name',
            'code',
        )


class CategoryCreateSerializer(ExtendedModelSerializer):
    class Meta:
        model = Category
        fields = (
            'id',
            'name',
            'code',
        )


class CategoryUpdateSerializer(ExtendedModelSerializer):
    class Meta:
        model = Category
        fields = (
            'id',
            'name',
            'code',
        )


class CategoryDeleteSerializer(serializers.Serializer):
    pass


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

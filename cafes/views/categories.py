from drf_spectacular.utils import extend_schema_view, extend_schema
from rest_framework import viewsets, mixins

from cafes.models.categories import CategoryCookingTime
from cafes.models.products import Category
from cafes.serializers.api.categories import (
    CategoryListSerializer,
    CategoryUpdateSerializer,
    CategoryCreateSerializer,
    CategoryRetrieveSerializer,
    CategoryCookingTimeRetrieveSerializer,
    CategoryCookingTimeListSerializer,
    CategoryCookingTimeCreateSerializer,
    CategoryCookingTimeUpdateSerializer)


@extend_schema_view(
    retrieve=extend_schema(summary='Получить категорию',
                           tags=['Товары: Категории']),
    list=extend_schema(summary='Список категорий', tags=['Товары: Категории']),
    create=extend_schema(summary='Создать категорию',
                         tags=['Товары: Категории']),
    partial_update=extend_schema(summary='Изменить категорию частично',
                                 tags=['Товары: Категории']),
)
class CategoryView(viewsets.GenericViewSet,
                   mixins.RetrieveModelMixin,
                   mixins.ListModelMixin,
                   mixins.UpdateModelMixin,
                   mixins.CreateModelMixin):
    queryset = Category.objects.all()
    serializer_class = CategoryListSerializer

    http_method_names = ('get', 'post', 'patch', 'delete',)

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return CategoryRetrieveSerializer
        elif self.action == 'list':
            return CategoryListSerializer
        elif self.action == 'create':
            return CategoryCreateSerializer
        elif self.action == 'partial_update':
            return CategoryUpdateSerializer


@extend_schema_view(
    retrieve=extend_schema(summary='Получить время приготовления категории',
                           tags=['Товары: Категории']),
    list=extend_schema(summary='Список времени приготовления категорий',
                       tags=['Категории товаров: Время приготовления']),
    create=extend_schema(summary='Добавить время приготовления категории',
                         tags=['Категории товаров: Время приготовления']),
    partial_update=extend_schema(
        summary='Изменить время приготовления категории',
        tags=['Категории товаров: Время приготовления']),
)
class CategoryCookingTimeView(viewsets.GenericViewSet,
                              mixins.RetrieveModelMixin,
                              mixins.ListModelMixin,
                              mixins.UpdateModelMixin,
                              mixins.CreateModelMixin):
    queryset = CategoryCookingTime.objects.all()
    serializer_class = CategoryCookingTimeListSerializer

    lookup_url_kwarg = 'cooking_time_id'

    http_method_names = ('get', 'post', 'patch', 'delete',)

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return CategoryCookingTimeRetrieveSerializer
        elif self.action == 'list':
            return CategoryCookingTimeListSerializer
        elif self.action == 'create':
            return CategoryCookingTimeCreateSerializer
        elif self.action == 'partial_update':
            return CategoryCookingTimeUpdateSerializer

    def get_queryset(self):
        category_id = self.kwargs.get('category_id')
        return CategoryCookingTime.objects.filter(category=category_id)

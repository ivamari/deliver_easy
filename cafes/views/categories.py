from drf_spectacular.utils import extend_schema_view, extend_schema
from rest_framework.permissions import IsAdminUser

from cafes.models.products import Category
from cafes.serializers.api.categories import (
    CategoryListSerializer,
    CategoryUpdateSerializer,
    CategoryCreateSerializer,
    CategoryRetrieveSerializer
)
from common.views.mixins import LCRUViewSet



@extend_schema_view(
    retrieve=extend_schema(summary='Получить категорию',
                           tags=['Товары: Категории']),
    list=extend_schema(summary='Список категорий', tags=['Товары: Категории']),
    create=extend_schema(summary='Создать категорию',
                         tags=['Товары: Категории']),
    partial_update=extend_schema(summary='Изменить категорию частично',
                                 tags=['Товары: Категории']),
)
class CategoryView(LCRUViewSet):
    permission_classes = [IsAdminUser]
    queryset = Category.objects.all()
    serializer_class = CategoryListSerializer

    http_method_names = ('get', 'post', 'patch', 'delete',)

    multi_serializer_class = {
        'list': CategoryListSerializer,
        'retrieve': CategoryRetrieveSerializer,
        'create': CategoryCreateSerializer,
        'update': CategoryUpdateSerializer,
        'partial_update': CategoryUpdateSerializer,
    }

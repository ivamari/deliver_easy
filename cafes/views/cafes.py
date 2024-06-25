from drf_spectacular.utils import extend_schema_view, extend_schema
from rest_framework.permissions import IsAuthenticated, IsAdminUser

from common.views.mixins import ListViewSet
from cafes.models.cafes import Cafe
from cafes.permissions import IsMyCafe, IsMyCafeDepartment
from cafes.serializers.api.cafes import (
    CafeRetrieveSerializer,
    CafeListSerializer,
    CafeCreateSerializer,
    CafeUpdateSerializer,
    CafeSearchListSerializer
)
from cafes.serializers.api.departments import (
    CafeDepartmentListSerializer,
    CafeDepartmentRetrieveSerializer,
    CafeDepartmentCreateUpdateSerializer
)
from cafes.views.nested.nested import BaseCafeView



@extend_schema_view(
    list=extend_schema(summary='Список кафе Search',
                       tags=['Search']),
)
class CafeSearchView(ListViewSet):
    """Список кафе с краткой информацией"""
    permission_classes = [IsAuthenticated]
    queryset = Cafe.objects.all()
    serializer_class = CafeSearchListSerializer


@extend_schema_view(
    retrieve=extend_schema(summary='Получить кафе', tags=['Кафе']),
    list=extend_schema(summary='Список кафе', tags=['Кафе']),
    create=extend_schema(summary='Создать кафе', tags=['Кафе']),
    update=extend_schema(summary='Изменить кафе', tags=['Кафе']),
    partial_update=extend_schema(summary='Изменить кафе частично',
                                 tags=['Кафе']),
)
class CafeView(BaseCafeView):
    permission_classes = [IsAdminUser]
    queryset = Cafe.objects.all()

    multi_serializer_class = {
        'list': CafeListSerializer,
        'retrieve': CafeRetrieveSerializer,
        'create': CafeCreateSerializer,
        'update': CafeUpdateSerializer,
        'partial_update': CafeUpdateSerializer,
    }

    multi_permission_classes = {
        'list': [IsMyCafe],
        'retrieve': [IsMyCafe],
        'create': [IsAdminUser],
        'update': [IsMyCafe],
        'partial_update': [IsMyCafe],
    }

    http_method_names = ('get', 'post', 'patch',)


@extend_schema_view(
    list=extend_schema(summary='Список кафе с отделами', tags=['Кафе: Отделы']),
    retrieve=extend_schema(summary='Получить кафе с отделами',
                           tags=['Кафе: Отделы']),
    update=extend_schema(summary='Добавить отдел в кафе',
                         tags=['Кафе: Отделы']),
)
class CafeDepartmentView(BaseCafeView):
    """Представление для кафе с отделами"""
    permission_classes = [IsMyCafeDepartment]
    queryset = Cafe.objects.all()

    multi_serializer_class = {
        'list': CafeDepartmentListSerializer,
        'retrieve': CafeDepartmentRetrieveSerializer,
        'update': CafeDepartmentCreateUpdateSerializer,
        'partial_update': CafeDepartmentCreateUpdateSerializer,
    }

    http_method_names = ('get', 'patch', 'put')

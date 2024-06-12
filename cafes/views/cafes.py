from django.db.models import Count, Case, When
from django_filters.rest_framework import DjangoFilterBackend
from drf_spectacular.utils import extend_schema_view, extend_schema
from rest_framework.filters import OrderingFilter, SearchFilter

from cafes.backends import MyCafe
from cafes.filters import CafeFilter
from cafes.models.cafes import Cafe
from cafes.permissions import IsMyCafe
from cafes.serializers.api.cafes import (CafeRetrieveSerializer,
                                         CafeListSerializer,
                                         CafeCreateSerializer,
                                         CafeUpdateSerializer,
                                         CafeSearchListSerializer)
from common.views.mixins import LCRUViewSet, ListViewSet


@extend_schema_view(
    list=extend_schema(summary='Список кафе Search',
                       tags=['Search']),
)
class CafeSearchView(ListViewSet):
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
class CafeView(LCRUViewSet):
    """Представление для кафе"""
    permission_classes = [IsMyCafe]
    queryset = Cafe.objects.all()
    serializer_class = CafeListSerializer

    http_method_names = ('get', 'post', 'patch',)

    multi_serializer_class = {
        'list': CafeListSerializer,
        'retrieve': CafeRetrieveSerializer,
        'create': CafeCreateSerializer,
        'update': CafeUpdateSerializer,
        'partial_update': CafeUpdateSerializer,
    }

    filter_backends = (
        OrderingFilter,
        SearchFilter,
        DjangoFilterBackend,
        MyCafe,
    )

    search_fields = ('name',)
    filterset_class = CafeFilter
    ordering = ('name', 'id',)

    def get_queryset(self):
        queryset = Cafe.objects.select_related(
            'owner',
        ).prefetch_related(
            'employees',
            'departments',
        ).annotate(
            # количество сотрудников в кафе
            pax=Count('employees', distinct=True),
            # количество отделов кафе
            departments_count=Count('departments', distinct=True),
            # может ли текущий пользователь управлять кафе
            can_manage=Case(
                When(owner=self.request.user, then=True),
                default=False,
            )
        )
        return queryset

from django.db.models import Count, Case, When
from django_filters.rest_framework import DjangoFilterBackend

from rest_framework.filters import OrderingFilter, SearchFilter

from cafes.backends import MyCafe
from cafes.filters import CafeFilter
from cafes.models.cafes import Cafe
from common.views.mixins import LCRUViewSet


class BaseCafeView(LCRUViewSet):
    queryset = Cafe.objects.all()

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
            # может ли текущий пользователь управлять кафе (если владелец)
            can_manage=Case(
                When(owner=self.request.user, then=True),
                default=False,
            )
        )
        return queryset

from drf_spectacular.utils import extend_schema_view, extend_schema
from rest_framework import viewsets, mixins

from cafes.models.departments import Department
from cafes.serializers.api.departments import (DepartmentListSerializer,
                                               DepartmentRetrieveSerializer,
                                               DepartmentCreateSerializer,
                                               DepartmentUpdateSerializer)


@extend_schema_view(
    retrieve=extend_schema(summary='Получить отдел кафе',
                           tags=['Кафе: Отделы']),
    list=extend_schema(summary='Список отделов', tags=['Кафе: Отделы']),
    create=extend_schema(summary='Создать отдел кафе', tags=['Кафе: Отделы']),
    partial_update=extend_schema(summary='Изменить отдел кафе частично',
                                 tags=['Кафе: Отделы']),
)
class DepartmentView(viewsets.GenericViewSet,
                     mixins.RetrieveModelMixin,
                     mixins.ListModelMixin,
                     mixins.UpdateModelMixin,
                     mixins.CreateModelMixin):
    queryset = Department.objects.all()
    serializer_class = DepartmentListSerializer

    lookup_url_kwarg = 'department_id'

    http_method_names = ('get', 'post', 'patch', 'delete',)

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return DepartmentRetrieveSerializer
        elif self.action == 'list':
            return DepartmentListSerializer
        elif self.action == 'create':
            return DepartmentCreateSerializer
        elif self.action == 'partial_update':
            return DepartmentUpdateSerializer

    def get_queryset(self):
        cafe_id = self.kwargs.get('cafe_id')
        return Department.objects.filter(cafe=cafe_id)

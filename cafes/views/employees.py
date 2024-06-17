from drf_spectacular.utils import extend_schema_view, extend_schema
from rest_framework import viewsets, mixins

from cafes.models.employees import Employee
from cafes.serializers.api.employees import (EmployeeListSerializer,
                                             EmployeeRetrieveSerializer,
                                             EmployeeCreateSerializer,
                                             EmployeeUpdateSerializer,
                                             EmployeeDeleteSerializer)


@extend_schema_view(
    list=extend_schema(summary='Список сотрудников кафе',
                       tags=['Кафе: Сотрудники']),
    retrieve=extend_schema(summary='Деталка сотрудника кафе',
                           tags=['Кафе: Сотрудники']),
    create=extend_schema(summary='Создать сотрудника кафе',
                         tags=['Кафе: Сотрудники']),
    partial_update=extend_schema(
        summary='Изменить сотрудника кафе частично',
        tags=['Кафе: Сотрудники']),
    destroy=extend_schema(summary='Удалить сотрудника из кафе',
                          tags=['Кафе: Сотрудники']),
)
class EmployeeView(viewsets.GenericViewSet,
                   mixins.ListModelMixin,
                   mixins.CreateModelMixin,
                   mixins.UpdateModelMixin,
                   mixins.DestroyModelMixin,
                   mixins.RetrieveModelMixin):
    queryset = Employee.objects.all()
    serializer_class = EmployeeListSerializer

    lookup_url_kwarg = 'employee_id'
    http_method_names = ('get', 'post', 'patch', 'delete', )

    def get_serializer_class(self):
        if self.action == 'list':
            return EmployeeListSerializer
        elif self.action == 'retrieve':
            return EmployeeRetrieveSerializer
        elif self.action == 'create':
            return EmployeeCreateSerializer
        elif self.action == 'update':
            return EmployeeUpdateSerializer
        elif self.action == 'partial_update':
            return EmployeeUpdateSerializer
        elif self.action == 'delete':
            return EmployeeDeleteSerializer

    def get_queryset(self):
        cafe_id = self.kwargs.get('cafe_id')
        return Employee.objects.filter(cafe=cafe_id)

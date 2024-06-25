from drf_spectacular.utils import extend_schema_view, extend_schema

from cafes.models.employees import Employee
from cafes.permissions import IsMyCafeEmployee
from cafes.serializers.api.employees import (
    EmployeeListSerializer,
    EmployeeRetrieveSerializer,
    EmployeeUpdateSerializer,
    EmployeeDeleteSerializer
)
from common.views.mixins import LCRUDViewSet



@extend_schema_view(
    list=extend_schema(summary='Список сотрудников кафе',
                       tags=['Кафе: Сотрудники']),
    retrieve=extend_schema(summary='Деталка сотрудника кафе',
                           tags=['Кафе: Сотрудники']),
    update=extend_schema(
        summary='Обновить должность сотрудника кафе',
        tags=['Кафе: Сотрудники']),
    partial_update=extend_schema(
        summary='Обновить должность сотрудника кафе',
        tags=['Кафе: Сотрудники']),
    destroy=extend_schema(summary='Удалить сотрудника из кафе',
                          tags=['Кафе: Сотрудники']),
)
class EmployeeView(LCRUDViewSet):
    permission_classes = [IsMyCafeEmployee]
    queryset = Employee.objects.all()

    lookup_url_kwarg = 'employee_id'
    http_method_names = ('get', 'post', 'patch', 'delete',)

    multi_serializer_class = {
        'list': EmployeeListSerializer,
        'retrieve': EmployeeRetrieveSerializer,
        'update': EmployeeUpdateSerializer,
        'partial_update': EmployeeUpdateSerializer,
        'delete': EmployeeDeleteSerializer,
    }

    def get_queryset(self):
        cafe_id = self.kwargs.get('cafe_id')
        return Employee.objects.filter(cafe=cafe_id)

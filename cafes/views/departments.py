from drf_spectacular.utils import extend_schema_view, extend_schema
from cafes.models.departments import Department

from cafes.serializers.api.departments import (
    DepartmentLittleListSerializer,
    CafeDepartmentCreateUpdateSerializer)
from common.views.mixins import LCRUViewSet


@extend_schema_view(
    list=extend_schema(summary='Список всех отделов', tags=['Отделы']),
)
class DepartmentView(LCRUViewSet):
    # permission_classes = [IsMyDepartment]
    queryset = Department.objects.all()
    serializer_class = CafeDepartmentCreateUpdateSerializer

    http_method_names = ('get', 'post', 'patch', )

    multi_serializer_class = {
        'list': DepartmentLittleListSerializer,
    }

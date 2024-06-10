from drf_spectacular.utils import extend_schema_view, extend_schema
from rest_framework import viewsets, mixins

from cafes.models.positions import Position
from cafes.serializers.api.positions import (PositionListSerializer,
                                             PositionRetrieveSerializer,
                                             PositionCreateSerializer,
                                             PositionUpdateSerializer)


@extend_schema_view(
    retrieve=extend_schema(summary='Получить должность',
                           tags=['Кафе: Должности']),
    list=extend_schema(summary='Список должностей', tags=['Кафе: Должности']),
    create=extend_schema(summary='Создать должность', tags=['Кафе: Должности']),
    partial_update=extend_schema(summary='Изменить должность частично',
                                 tags=['Кафе: Должности']),
)
class PositionView(viewsets.GenericViewSet,
                   mixins.RetrieveModelMixin,
                   mixins.ListModelMixin,
                   mixins.UpdateModelMixin,
                   mixins.CreateModelMixin):
    queryset = Position.objects.all()
    serializer_class = PositionListSerializer

    lookup_url_kwarg = 'position_id'

    http_method_names = ('get', 'post', 'patch', 'delete',)

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return PositionRetrieveSerializer
        elif self.action == 'list':
            return PositionListSerializer
        elif self.action == 'create':
            return PositionCreateSerializer
        elif self.action == 'partial_update':
            return PositionUpdateSerializer

    def get_queryset(self):
        department_id = self.kwargs.get('department_id')
        return Position.objects.filter(department=department_id)


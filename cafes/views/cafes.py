from drf_spectacular.utils import extend_schema_view, extend_schema
from rest_framework import viewsets, mixins

from cafes.models.cafes import Cafe
from cafes.serializers.api.cafes import CafeRetrieveSerializer, \
    CafeListSerializer, CafeCreateSerializer, CafeUpdateSerializer


@extend_schema_view(
    retrieve=extend_schema(summary='Получить кафе', tags=['Кафе']),
    list=extend_schema(summary='Список кафе', tags=['Кафе']),
    create=extend_schema(summary='Создать кафе', tags=['Кафе']),
    update=extend_schema(summary='Изменить кафе', tags=['Кафе']),
    partial_update=extend_schema(summary='Изменить кафе частично',
                                 tags=['Кафе']),
)
class CafeViewSet(viewsets.GenericViewSet,
                  mixins.RetrieveModelMixin,
                  mixins.ListModelMixin,
                  mixins.UpdateModelMixin,
                  mixins.CreateModelMixin):
    queryset = Cafe.objects.all()
    serializer_class = CafeListSerializer

    http_method_names = ('get', 'post', 'patch',)

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return CafeRetrieveSerializer
        elif self.action == 'list':
            return CafeListSerializer
        elif self.action == 'create':
            return CafeCreateSerializer
        elif self.action == 'update':
            return CafeUpdateSerializer
        elif self.action == 'partial_update':
            return CafeUpdateSerializer

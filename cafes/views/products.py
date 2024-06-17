from drf_spectacular.utils import extend_schema_view, extend_schema

from cafes.models.products import Product
from cafes.serializers.api.products import (ProductCafeRetrieveSerializer,
                                            ProductCafeListSerializer,
                                            ProductCreateSerializer,
                                            ProductUpdateSerializer,
                                            ProductListSerializer,
                                            ProductRetrieveSerializer)
from common.views.mixins import LCRUViewSet


@extend_schema_view(
    retrieve=extend_schema(summary='Получить определенный товар кафе',
                           tags=['Кафе: Товары']),
    list=extend_schema(summary='Список товаров определенного кафе',
                       tags=['Кафе: Товары']),
    create=extend_schema(summary='Добавить товар в кафе',
                         tags=['Кафе: Товары']),
)
class ProductCafeView(LCRUViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductCafeListSerializer

    lookup_url_kwarg = 'product_id'

    http_method_names = ('get', 'post', 'patch', 'delete',)

    multi_serializer_class = {
        'list': ProductCafeListSerializer,
        'retrieve': ProductCafeRetrieveSerializer,
    }

    def get_queryset(self):
        cafe_id = self.kwargs.get('cafe_id')
        return Product.objects.filter(cafe=cafe_id)


@extend_schema_view(
    retrieve=extend_schema(summary='Получить товар',
                           tags=['Товары']),
    list=extend_schema(summary='Список товаров',
                       tags=['Товары']),
    create=extend_schema(summary='Добавить товар',
                         tags=['Товары']),
    partial_update=extend_schema(summary='Изменить товар',
                                 tags=['Товары']),
)
class ProductView(LCRUViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductListSerializer

    lookup_url_kwarg = 'product_id'

    http_method_names = ('get', 'post', 'patch', 'delete',)

    multi_serializer_class = {
        'create': ProductCreateSerializer,
        'list': ProductListSerializer,
        'retrieve': ProductRetrieveSerializer,
        'update': ProductUpdateSerializer,
        'partial_update': ProductUpdateSerializer,
    }

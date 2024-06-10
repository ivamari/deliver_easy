from drf_spectacular.utils import extend_schema_view, extend_schema
from rest_framework import viewsets, mixins

from cafes.models.products import Product
from cafes.serializers.api.products import (ProductCafeRetrieveSerializer,
                                            ProductCafeListSerializer,
                                            ProductCreateSerializer,
                                            ProductUpdateSerializer,
                                            ProductListSerializer,
                                            ProductRetrieveSerializer)


@extend_schema_view(
    retrieve=extend_schema(summary='Получить определенный товар кафе',
                           tags=['Кафе: Товары']),
    list=extend_schema(summary='Список товаров определенного кафе',
                       tags=['Кафе: Товары']),
    create=extend_schema(summary='Добавить товар в кафе',
                         tags=['Кафе: Товары']),
    # partial_update=extend_schema(summary='Изменить товар',
    #                              tags=['Кафе: Товары']),
)
class ProductCafeView(viewsets.GenericViewSet,
                      mixins.RetrieveModelMixin,
                      mixins.ListModelMixin,
                      mixins.UpdateModelMixin,
                      mixins.CreateModelMixin):
    queryset = Product.objects.all()
    serializer_class = ProductCafeListSerializer

    lookup_url_kwarg = 'product_id'

    http_method_names = ('get', 'post', 'patch', 'delete',)

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return ProductCafeRetrieveSerializer
        elif self.action == 'list':
            return ProductCafeListSerializer
        # elif self.action == 'create':
        #     return ProductCafeCreateSerializer

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
class ProductView(viewsets.GenericViewSet,
                  mixins.RetrieveModelMixin,
                  mixins.ListModelMixin,
                  mixins.UpdateModelMixin,
                  mixins.CreateModelMixin):
    queryset = Product.objects.all()
    serializer_class = ProductListSerializer

    lookup_url_kwarg = 'product_id'

    http_method_names = ('get', 'post', 'patch', 'delete',)

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return ProductRetrieveSerializer
        elif self.action == 'list':
            return ProductListSerializer
        elif self.action == 'create':
            return ProductCreateSerializer
        elif self.action == 'partial_update':
            return ProductUpdateSerializer

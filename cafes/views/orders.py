from django.shortcuts import get_object_or_404
from drf_spectacular.utils import extend_schema_view, extend_schema
from rest_framework import mixins
from rest_framework.generics import GenericAPIView, ListAPIView, RetrieveAPIView
from rest_framework.permissions import IsAuthenticated, IsAdminUser

from cafes.models.orders import Order
from cafes.permissions import IsMyOrder
from cafes.serializers.api.orders import (OrderCreateSerializer,
                                          OrderRetrieveSerializer)


@extend_schema_view(
    post=extend_schema(summary='Создать заказ', tags=['Заказы']),
)
class OrderCreateView(GenericAPIView,
                      mixins.CreateModelMixin):
    """Представление для создания заказа"""
    permission_classes = [IsAuthenticated]
    queryset = Order.objects.all()
    serializer_class = OrderCreateSerializer

    http_method_names = ('post', 'get',)

    def get_object(self):
        user = self.request.user

        return get_object_or_404(
            Order, user_id=user)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


@extend_schema_view(
    get=extend_schema(summary='Посмотреть заказы пользователя', tags=['Заказы']),
)
class OrderListView(ListAPIView):
    """Представление для просмотра списка заказов пользователя
    по id пользователя"""
    serializer_class = OrderRetrieveSerializer
    permission_classes = [IsAdminUser]

    def get_queryset(self):
        client_id = self.kwargs.get('client_id')
        return Order.objects.filter(user_id=client_id)

    http_method_names = ['get']


@extend_schema_view(
    get=extend_schema(summary='Посмотреть заказ', tags=['Заказы']),
)
class MeOrderRetrieveView(RetrieveAPIView):
    """Получение заказа пользователя по id заказа"""
    queryset = Order.objects.all()
    permission_classes = [IsMyOrder]
    serializer_class = OrderRetrieveSerializer
    http_method_names = ('get',)

    def get_queryset(self):
        return Order.objects.filter(user=self.request.user)

    def get_object(self):
        queryset = self.get_queryset()
        order_id = self.kwargs.get('order_id')
        return get_object_or_404(queryset, id=order_id)


@extend_schema_view(
    get=extend_schema(summary='Посмотреть список своих заказов', tags=['Заказы']),
)
class MeOrderListView(ListAPIView):
    """Получение списка своих заказов/me"""
    queryset = Order.objects.all()
    serializer_class = OrderRetrieveSerializer
    http_method_names = ('get',)

    def get_queryset(self):
        return Order.objects.filter(user=self.request.user)

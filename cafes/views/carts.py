from django.shortcuts import get_object_or_404
from drf_spectacular.utils import extend_schema_view, extend_schema
from rest_framework import mixins
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response

from cafes.models.carts import Cart
from cafes.serializers.api.carts import (CartRetrieveSerializer,
                                         MeCartRetrieveSerializer)


@extend_schema_view(
    get=extend_schema(
        summary='Получить корзину пользователя по id пользователя',
        tags=['Корзины']),
)
class CartView(GenericAPIView, mixins.RetrieveModelMixin):
    """Представление для получения корзины пользователя по id пользователя"""
    queryset = Cart.objects.all()
    serializer_class = CartRetrieveSerializer

    http_method_names = ('get',)

    def get_object(self):
        client_id = self.kwargs.get('client_id')
        return get_object_or_404(Cart, user_id=client_id)

    def get(self, request, *args, **kwargs):
        cart = self.get_object()
        serializer = self.get_serializer(cart)
        return Response(serializer.data)


@extend_schema_view(
    get=extend_schema(
        summary='Получить свою корзину',
        tags=['Корзины']),
)
class MeCartView(GenericAPIView, mixins.RetrieveModelMixin):
    """Получение корзины пользователя /me"""
    # permission_classes = [IsNotCorporate]
    queryset = Cart.objects.all()
    serializer_class = MeCartRetrieveSerializer
    http_method_names = ('get',)

    def get_object(self):
        user = self.request.user

        return get_object_or_404(
            Cart, user_id=user)

    def get(self, request, *args, **kwargs):
        cart = self.get_object()
        serializer = self.get_serializer(cart)
        return Response(serializer.data)

# сделать так, чтобы если не было товаров в корзине, выводилось "корзина пуста"

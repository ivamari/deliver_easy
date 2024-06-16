from django.shortcuts import get_object_or_404
from drf_spectacular.utils import extend_schema_view, extend_schema
from rest_framework import mixins, status, generics
from rest_framework.generics import GenericAPIView
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response

from cafes.models.carts import Cart, CartProduct
from cafes.permissions import IsMyCart
from cafes.serializers.api.carts import (CartUserRetrieveSerializer,
                                         MeCartRetrieveSerializer,
                                         CartProductCreateUpdateSerializer,
                                         CartProductDeleteSerializer,
                                         IncreaseCartProductQuantitySerializer,
                                         ReduceCartProductQuantitySerializer, )


@extend_schema_view(
    get=extend_schema(
        summary='Получить корзину пользователя по id пользователя',
        tags=['Корзины']),
)
class CartView(GenericAPIView, mixins.RetrieveModelMixin):
    """Представление для получения корзины пользователя по id пользователя"""
    queryset = Cart.objects.all()
    permission_classes = [IsAdminUser]
    serializer_class = CartUserRetrieveSerializer

    http_method_names = ('get',)

    def get_object(self):
        client_id = self.kwargs.get('client_id')
        return get_object_or_404(Cart, user_id=client_id)

    def get(self, request, *args, **kwargs):
        cart = self.get_object()
        serializer = self.get_serializer(cart)
        return Response(serializer.data)


@extend_schema_view(
    get=extend_schema(summary='Получить свою корзину', tags=['Корзины']),
    put=extend_schema(summary='Добавить товар в корзину', tags=['Корзины']),
    delete=extend_schema(summary='Удалить товар из корзины', tags=['Корзины']),
)
class MeCartView(GenericAPIView,
                 mixins.RetrieveModelMixin,
                 mixins.UpdateModelMixin,):
    """Получение корзины пользователя /me"""
    permission_classes = [IsMyCart]
    queryset = Cart.objects.all()
    serializer_class = CartProductCreateUpdateSerializer
    http_method_names = ('get', 'patch', 'put',)

    multi_serializer_class = {
        'retrieve': MeCartRetrieveSerializer,
        'update': CartProductCreateUpdateSerializer,
        'partial_update': CartProductCreateUpdateSerializer,
    }

    def get_object(self):
        user = self.request.user

        return get_object_or_404(
            Cart, user_id=user)

    def get(self, request, *args, **kwargs):
        cart = self.get_object()
        serializer = self.get_serializer(cart)
        return Response(serializer.data)

    def put(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = CartProductCreateUpdateSerializer(instance,
                                                       data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)


@extend_schema_view(
    delete=extend_schema(summary='Удалить товар из корзины', tags=['Корзины']),
)
class MeCartDeleteView(GenericAPIView,
                       mixins.DestroyModelMixin):
    """Удалить товар из корзины/me"""
    permission_classes = [IsMyCart]
    queryset = Cart.objects.all()
    serializer_class = CartProductDeleteSerializer
    http_method_names = ('delete', )

    multi_serializer_class = {
        'destroy': CartProductDeleteSerializer,
    }

    def delete(self, request, *args, **kwargs):
        product_id = kwargs.get('product_id')
        data = {'product_id': product_id}

        serializer = self.get_serializer(data=data,
                                         context={'request': request})
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(status=status.HTTP_204_NO_CONTENT)


@extend_schema_view(
    patch=extend_schema(summary='Увеличить количество товара в корзине на 1', tags=['Корзины']),
)
class IncreaseProductQuantityView(generics.GenericAPIView):
    """Увеличить количество товара в корзине на 1/me"""
    permission_classes = [IsMyCart]
    queryset = CartProduct.objects.all()
    serializer_class = IncreaseCartProductQuantitySerializer
    http_method_names = ['patch']

    def patch(self, request, *args, **kwargs):
        product_id = kwargs.get('product_id')
        data = {'product_id': product_id}

        serializer = self.get_serializer(data=data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(status=status.HTTP_200_OK)


@extend_schema_view(
    patch=extend_schema(summary='Уменьшить количество товара в корзине на 1', tags=['Корзины']),
)
class ReduceProductQuantityView(generics.GenericAPIView):
    """Уменьшить количество товара в корзине на 1/me"""
    permission_classes = [IsMyCart]
    queryset = CartProduct.objects.all()
    serializer_class = ReduceCartProductQuantitySerializer
    http_method_names = ['patch']

    def patch(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(status=status.HTTP_200_OK)

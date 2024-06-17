# from drf_spectacular.utils import extend_schema_view, extend_schema
# from requests import Response
# from rest_framework import mixins, status
# from rest_framework.generics import GenericAPIView
#
# from cafes.models.orders import Order
# from cafes.serializers.api.orders import OrderCreateSerializer
# from common.views.mixins import LCRUViewSet
#
#
# @extend_schema_view(
#     post=extend_schema(summary='Создать заказ', tags=['Заказы']),
# )
# class MeOrderView(GenericAPIView,
#                   mixins.CreateModelMixin,
#                   ):
#     """Получение корзины пользователя /me"""
#     queryset = Order.objects.all()
#     http_method_names = ('post', )
#
#     multi_serializer_class = {
#         'create': OrderCreateSerializer,
#     }
#
#

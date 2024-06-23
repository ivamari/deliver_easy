# from drf_spectacular.utils import extend_schema_view, extend_schema
# from rest_framework import mixins
# from rest_framework.generics import GenericAPIView
#
# from cafes.models.orders import Order
# # from cafes.serializers.api.orders import OrderCreateSerializer
#
#
# @extend_schema_view(
#     post=extend_schema(summary='Создать заказ', tags=['Заказы']),
# )
# class OrderView(GenericAPIView,
#                 mixins.CreateModelMixin,
#                 mixins.ListModelMixin):
#     queryset = Order.objects.all()
#     serializer_class = OrderCreateSerializer
#
#     http_method_names = ('post', )
#
#     def post(self, request, *args, **kwargs):
#         return self.create(request, *args, **kwargs)
#
#     # multi_serializer_class = {
#     #     'create': OrderCreateSerializer,
#     # }

# from django.contrib.auth import get_user_model
#
# from cafes.models.orders import Order, OrderProduct
# from users.serializers.nested.users import UserShortSerializer
# from rest_framework_gis.serializers import GeoFeatureModelSerializer
#
# User = get_user_model()
#
#
# class OrderCreateSerializer(GeoFeatureModelSerializer):
#     """Сериализатор для создания заказа"""
#     user = UserShortSerializer(read_only=True)
#
#     class Meta:
#         model = Order
#         fields = ('id',
#                   'user',
#                   'location',
#                   'order_date',
#                   'order_time',
#                   'products')
#         geo_field = 'location'
#         read_only_fields = ('order_date', 'order_time', 'products', 'user')
#         id_field = False
#
#     def create(self, validated_data):
#         order = super().create(validated_data)
#         self.create_order_from_cart(order)
#         return order
#
#     def create_order_from_cart(self, order):
#         user = self.context['request'].user
#         cart = user.user_cart(order)
#
#         if cart:
#             for cart_product in cart.cart_products.all():
#                 OrderProduct.objects.create(
#                     order=order,
#                     product=cart_product.product,
#                     amount=cart_product.amount,
#                 )

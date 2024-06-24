from django.contrib.auth import get_user_model
from rest_framework import serializers

from cafes.models.orders import Order
from cafes.serializers.nested.cafes import CafeShortSerializer
from cafes.serializers.nested.products import ProductShortSerializer
from rest_framework_gis.serializers import GeoFeatureModelSerializer

User = get_user_model()


class OrderListSerializer(GeoFeatureModelSerializer):
    """Сериализатор для вывода списка заказов пользователя"""
    nearest_cafe = CafeShortSerializer()
    products = ProductShortSerializer(many=True)

    class Meta:
        model = Order
        fields = (
            'user',
            'location',
            'order_date',
            'order_time',
            'nearest_cafe',
            'products',
        )
        geo_field = 'location'


class OrderRetrieveSerializer(GeoFeatureModelSerializer):
    """Сериализатор для вывода информации о заказе"""
    nearest_cafe = CafeShortSerializer()
    products = ProductShortSerializer(many=True)

    class Meta:
        model = Order
        fields = (
            'user',
            'location',
            'order_date',
            'order_time',
            'nearest_cafe',
            'products',
        )
        geo_field = 'location'


class OrderCreateSerializer(GeoFeatureModelSerializer):
    """Сериализатор для создания заказа"""

    user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())

    class Meta:
        model = Order
        fields = (
            'user',
            'location'
        )
        geo_field = 'location'

    def to_representation(self, instance):
        request = self.context.get('request')
        return OrderRetrieveSerializer(instance,
                                       context={
                                           'request': request}).data

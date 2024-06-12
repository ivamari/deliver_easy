from rest_framework import serializers

from cafes.models.products import Product


class ProductShortSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = (
            'id',
            'name')

from rest_framework import serializers

from cafes.models.cafes import Cafe


class CategoryShortSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cafe
        fields = (
            'id',
            'name')


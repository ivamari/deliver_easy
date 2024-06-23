from rest_framework import serializers

from cafes.models.cafes import Cafe


class CafeShortSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cafe
        fields = (
            'id',
            'name')

from rest_framework import serializers

from cafes.models.positions import Position


class PositionShortSerializer(serializers.ModelSerializer):
    class Meta:
        model = Position
        fields = (
            'id',
            'name',
        )

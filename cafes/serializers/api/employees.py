from django.contrib.auth import get_user_model
from rest_framework import serializers

from cafes.models.employees import Employee
from cafes.models.positions import Position

from cafes.serializers.nested.cafes import CafeShortSerializer
from cafes.serializers.nested.positions import PositionShortSerializer

from common.serializers.mixins import ExtendedModelSerializer
from users.serializers.nested.users import UserEmployeeSerializer

import logging


logger = logging.getLogger(__name__)

User = get_user_model()


class EmployeeListSerializer(ExtendedModelSerializer):
    """Сериализатор для списка сотрудников кафе"""
    user = UserEmployeeSerializer()
    cafe = CafeShortSerializer()
    position = PositionShortSerializer()

    class Meta:
        model = Employee
        fields = (
            'id',
            'user',
            'cafe',
            'department',
            'position',
        )


class EmployeeRetrieveSerializer(ExtendedModelSerializer):
    """Сериализатор для получения сотрудника кафе"""
    user = UserEmployeeSerializer()
    cafe = CafeShortSerializer()
    position = PositionShortSerializer()

    class Meta:
        model = Employee
        fields = (
            'id',
            'user',
            'cafe',
            'department',
            'position'
        )


class EmployeeUpdateSerializer(ExtendedModelSerializer):
    """Сериализатор для обновления должности сотрудника кафе"""
    position = serializers.PrimaryKeyRelatedField(
        queryset=Position.objects.all())

    class Meta:
        model = Employee
        fields = (
            'position',
        )

    def to_representation(self, instance):
        request = self.context.get('request')
        return EmployeeRetrieveSerializer(
            instance, context={'request': request}).data


class EmployeeDeleteSerializer(serializers.Serializer):
    """Сериализатор для удаления сотрудника кафе"""
    pass

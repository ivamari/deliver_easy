from django.contrib.auth import get_user_model
from rest_framework import serializers
from rest_framework.exceptions import ParseError

from cafes.models.departments import Department
from cafes.models.positions import Position
from cafes.serializers.nested.departments import DepartmentShortSerializer
from common.serializers.mixins import ExtendedModelSerializer

User = get_user_model()


class PositionListSerializer(ExtendedModelSerializer):
    """Сериализатор для списка должностей"""
    department = DepartmentShortSerializer()

    class Meta:
        model = Position
        fields = (
            'id',
            'name',
            'department',
        )


class PositionRetrieveSerializer(ExtendedModelSerializer):
    """Сериализатор для получения должности"""
    department = DepartmentShortSerializer()

    class Meta:
        model = Position
        fields = (
            'id',
            'name',
            'department',
        )


class PositionCreateSerializer(ExtendedModelSerializer):
    """Сериализатор для создания должности"""
    department = serializers.PrimaryKeyRelatedField(
        queryset=Department.objects.all(), source='positions_department')

    class Meta:
        model = Position
        fields = (
            'id',
            'name',
            'department',
        )

    def validate_name(self, value):
        if self.Meta.model.objects.filter(name=value).exists():
            raise ParseError(
                'Такая должность уже существует.'
            )
        return value


class PositionUpdateSerializer(ExtendedModelSerializer):
    """Сериализатор для обновления должности"""
    department = DepartmentShortSerializer(read_only=True)

    class Meta:
        model = Position
        fields = (
            'id',
            'name',
            'department',
        )

    def validate_name(self, value):
        instance = self.instance
        if instance and instance.name == value:
            return value
        if Position.objects.filter(name=value).exists():
            raise ParseError("Должность с таким названием уже существует.")
        return value



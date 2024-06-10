from django.contrib.auth import get_user_model
from rest_framework import serializers

from cafes.models.cafes import Cafe
from cafes.models.departments import Department
from cafes.serializers.nested.cafes import CafeShortSerializer
from common.serializers.mixins import ExtendedModelSerializer
from users.serializers.nested.users import UserShortSerializer


User = get_user_model()


class DepartmentListSerializer(ExtendedModelSerializer):
    manager = UserShortSerializer()
    cafe = CafeShortSerializer()

    class Meta:
        model = Department
        fields = (
            'id',
            'name',
            'cafe',
            'manager'
        )


class DepartmentRetrieveSerializer(ExtendedModelSerializer):
    manager = UserShortSerializer()
    cafe = CafeShortSerializer()

    class Meta:
        model = Department
        fields = (
            'id',
            'name',
            'cafe',
            'manager'
        )


class DepartmentCreateSerializer(ExtendedModelSerializer):
    cafe = serializers.PrimaryKeyRelatedField(
        queryset=Cafe.objects.all())
    manager = serializers.PrimaryKeyRelatedField(
        queryset=User.objects.all()
    )

    class Meta:
        model = Department
        fields = (
            'id',
            'name',
            'cafe',
            'manager'
        )


class DepartmentUpdateSerializer(ExtendedModelSerializer):
    cafe = serializers.PrimaryKeyRelatedField(
        queryset=Cafe.objects.all())
    manager = serializers.PrimaryKeyRelatedField(
        queryset=User.objects.all()
    )

    class Meta:
        model = Department
        fields = (
            'id',
            'name',
            'cafe',
            'manager'
        )


class DepartmentDeleteSerializer(serializers.Serializer):
    pass

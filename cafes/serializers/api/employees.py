from django.contrib.auth import get_user_model
from django.db import transaction
from rest_framework import serializers
from rest_framework.exceptions import ParseError

from cafes.models.cafes import Cafe
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
    user = UserEmployeeSerializer()
    cafe = CafeShortSerializer()
    position = PositionShortSerializer()

    class Meta:
        model = Employee
        fields = (
            'id',
            'user',
            'cafe',
            'position'
        )


class EmployeeRetrieveSerializer(ExtendedModelSerializer):
    user = UserEmployeeSerializer()
    cafe = CafeShortSerializer()
    position = PositionShortSerializer()

    class Meta:
        model = Employee
        fields = (
            'id',
            'user',
            'cafe',
            'position'
        )


class EmployeeCreateSerializer(ExtendedModelSerializer):
    first_name = serializers.CharField(write_only=True)
    last_name = serializers.CharField(write_only=True)
    email = serializers.EmailField(write_only=True)
    password = serializers.CharField(write_only=True)

    class Meta:
        model = Employee
        fields = (
            'id',
            'first_name',
            'last_name',
            'email',
            'password',
            'position'
        )

    def validate(self, attrs):
        request = self.context.get('request')
        current_user = request.user
        cafe_id = self.context['view'].kwargs.get('pk')
        cafe = Cafe.objects.filter(id=cafe_id, owner=current_user).first()

        if not cafe:
            raise ParseError('Такого кафе не найдено.')

        attrs['cafe'] = cafe

        return attrs

    def create(self, validated_data):
        user_data = {
            'first_name': validated_data.pop('first_name'),
            'last_name': validated_data.pop('last_name'),
            'email': validated_data.pop('email'),
            'password': validated_data.pop('password'),
            'is_work_account': True
        }

        with transaction.atomic():
            user = User.objects.create_user(**user_data)
            validated_data['user'] = user

            instance = super().create(validated_data)

        return instance


class EmployeeUpdateSerializer(ExtendedModelSerializer):
    position = serializers.PrimaryKeyRelatedField(
        queryset=Position.objects.all())

    class Meta:
        model = Employee
        fields = (
            'cafe',
            'position',
        )


class EmployeeDeleteSerializer(serializers.Serializer):
    pass

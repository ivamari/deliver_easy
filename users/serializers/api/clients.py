from datetime import timedelta

from django.utils import timezone
from rest_framework import serializers
from django.contrib.auth import get_user_model
from rest_framework.exceptions import ParseError

User = get_user_model()


class RegistrationClientSerializer(serializers.ModelSerializer):
    """Сериализатор для регистрации пользователя"""

    # сделать регистрацию по номеру с подтверждением
    # сделать валидацию для даты рождения

    class Meta:
        model = User
        fields = (
            'first_name',
            'phone_number',
            'birth_day',
        )

    def validate_birth_year(self, value):
        now = timezone.now().date()
        if not 14 <= now - value <= 85:
            raise ParseError(
                'Проверьте дату рождения'
            )
        return value

    def create(self, validated_data):
        user = User.objects.create(**validated_data)
        return user


class MeClientSerializer(serializers.ModelSerializer):
    """Сериализатор для получения профиля клиента"""

    class Meta:
        model = User
        fields = (
            'id',
            'first_name',
            'email',
            'phone_number',
            'birth_day',
        )


class MeClientUpdateSerializer(serializers.ModelSerializer):
    """Сериализатор для изменения профиля клиента"""
    email = serializers.EmailField()

    # сделать изменение номера телефона с подтверждением
    # сделать изменение почты с подтверждением

    class Meta:
        model = User
        fields = (
            'id',
            'first_name',
            'email',
            'phone_number',
            'birth_day',
        )

    def validate_birth_day(self, value):
        now = timezone.now().date()
        age = (now - value).days // 365
        if not (14 < age < 85):
            raise ParseError(
                'Проверьте дату рождения. Возраст должен быть в пределах от 14 до 85 лет'
            )
        return value

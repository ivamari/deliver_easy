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

    class Meta:
        model = User
        fields = (
            'id',
            'first_name',
            'email',
            'phone_number',
            'birth_day',
        )

    def validate_email(self, value):
        email = value.lower()
        if User.objects.filter(email=email).exists():
            raise ParseError(
                'Пользователь с такой почтой уже зарегистрирован.'
            )
        return email

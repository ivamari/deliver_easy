from django.contrib.auth.password_validation import validate_password
from django.utils import timezone
from django.contrib.auth import get_user_model

from rest_framework import serializers
from rest_framework.exceptions import ParseError


User = get_user_model()


class RegistrationClientSerializer(serializers.ModelSerializer):
    """Сериализатор для регистрации пользователя"""

    email = serializers.EmailField()
    password = serializers.CharField(
        style={'input_type': 'password'},
        write_only=True
    )

    class Meta:
        model = User
        fields = (
            'first_name',
            'last_name',
            'password',
            'phone_number',
            'email',
            'birth_day',
            'username'
        )

    def validate_birth_day(self, value):
        now = timezone.now().date()
        age = (now - value).days / 365.25
        if not 14 <= age <= 85:
            raise serializers.ValidationError(
                'Проверьте дату рождения. '
                'Пользователь должен быть в возрасте от 14 до 85 лет.'
            )
        return value

    def validate_password(self, value):
        validate_password(value)
        return value

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        user = User.objects.create(**validated_data)
        if password:
            user.set_password(password)
            user.save()
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
            'last_name',
            'password',
            'phone_number',
            'email',
            'birth_day',
            'username'
        )

    def validate_birth_day(self, value):
        now = timezone.now().date()
        age = (now - value).days // 365
        if not (14 < age < 85):
            raise ParseError(
                'Проверьте дату рождения. '
                'Возраст должен быть в пределах от 14 до 85 лет'
            )
        return value


class ClientSerializer(serializers.ModelSerializer):
    """Сериализатор для получения профиля клиента по id"""

    class Meta:
        model = User
        fields = (
            'id',
            'first_name',
            'email',
            'phone_number',
            'birth_day',
        )

from rest_framework import serializers
from django.contrib.auth import get_user_model

User = get_user_model()


class RegistrationUserSerializer(serializers.ModelSerializer):
    """Сериализатор для регистрации пользователя"""
    # сделать вход по номеру с подтверждением
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

from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers
from django.contrib.auth import get_user_model
from rest_framework.exceptions import ParseError

User = get_user_model()


class RegistrationEmployeeSerializer(serializers.ModelSerializer):
    """Сериализатор для регистрации сотрудника"""
    # сделать подтверждение почты и подтверждение номера телефона
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
        )

    def validate_email(self, value):
        email = value.lower()
        if User.objects.filter(email=email).exists():
            raise ParseError(
                'Пользователь с такой почтой уже зарегистрирован.'
            )
        return email

    def validate_password(self, value):
        validate_password(value)
        return value

    def create(self, validated_data):
        user = User.objects.create(**validated_data)
        user.is_work_account = True
        user.save()
        return user


class ChangePasswordSerializer(serializers.ModelSerializer):
    """Сериализатор для смены пароля сотрудником"""
    old_password = serializers.CharField(write_only=True)
    new_password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = (
            'old_password',
            'new_password',
        )

    def validate(self, attrs):
        user = self.instance
        old_password = attrs.pop('old_password')
        if not user.check_password(old_password):
            raise ParseError(
                'Проверьте правильно введенного текущего пароля'
            )
        return attrs

    def validate_new_password(self, value):
        validate_password(value)
        return value

    def update(self, instance, validated_data):
        password = validated_data.pop('new_password')
        instance.set_password(password)
        instance.save()
        return instance


class MeEmployeeSerializer(serializers.ModelSerializer):
    """Сериализатор для получения профиля сотрудника"""

    class Meta:
        model = User
        fields = (
            'id',
            'first_name',
            'last_name',
            'email',
            'phone_number',
            'birth_day',
        )


class MeEmployeeUpdateSerializer(serializers.ModelSerializer):
    """Сериализатор для изменения профиля сотрудника"""
    email = serializers.EmailField()

    class Meta:
        model = User
        fields = (
            'id',
            'first_name',
            'last_name',
            'email',
            'phone_number',
            'birth_day',
        )

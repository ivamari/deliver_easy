from django.contrib.auth import get_user_model
from django.contrib.auth.password_validation import validate_password
from django.utils import timezone

from rest_framework import serializers
from rest_framework.exceptions import ParseError


User = get_user_model()


class RegistrationEmployeeSerializer(serializers.ModelSerializer):
    """Сериализатор для регистрации сотрудника"""
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
            'username',
            'password',
            'phone_number',
            'email',
            'birth_day',
            'is_work_account',
        )

    def validate(self, data):
        data['is_work_account'] = True
        return data

    def validate_birth_year(self, value):
        now = timezone.now().date()
        if not 14 <= now - value <= 85:
            raise ParseError(
                'Проверьте дату рождения'
            )
        return value

    def validate_password(self, value):
        validate_password(value)
        return value

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        user = User.objects.create(**validated_data)
        user.is_work_account = True
        if password:
            user.set_password(password)
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
            'is_work_account',
        )


class EmployeeUpdateRetrieveSerializer(serializers.ModelSerializer):
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

    def validate_birth_day(self, value):
        now = timezone.now().date()
        age = (now - value).days // 365
        if not (14 < age < 85):
            raise ParseError(
                'Проверьте дату рождения. '
                'Возраст должен быть в пределах от 14 до 85 лет'
            )
        return value

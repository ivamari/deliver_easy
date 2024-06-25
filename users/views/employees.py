from drf_spectacular.utils import extend_schema_view, extend_schema
from rest_framework import generics
from rest_framework.generics import RetrieveUpdateAPIView
from rest_framework.permissions import IsAdminUser

from django.contrib.auth import get_user_model

from users.permissions import IsEmployee
from users.serializers.api.employees import (
    RegistrationEmployeeSerializer,
    MeEmployeeSerializer,
    EmployeeUpdateRetrieveSerializer
)


User = get_user_model()


@extend_schema_view(
    post=extend_schema(summary='Регистрация сотрудника',
                       tags=['Аутентификация & Авторизация: Сотрудники']),
)
class RegistrationEmployeeView(generics.CreateAPIView):
    """Регистрация сотрудника"""
    queryset = User.objects.all()
    permission_classes = [IsAdminUser]
    serializer_class = RegistrationEmployeeSerializer


@extend_schema_view(
    get=extend_schema(summary='Профиль сотрудника', tags=['Сотрудники']),
)
class MeEmployeeView(RetrieveUpdateAPIView):
    """Получение профиля сотрудника/me"""
    permission_classes = [IsEmployee]
    queryset = User.objects.all()
    serializer_class = MeEmployeeSerializer
    http_method_names = ('get',)

    def get_object(self):
        return self.request.user


@extend_schema_view(
    patch=extend_schema(summary='Изменить частично профиль сотрудника',
                        tags=['Сотрудники']),
    get=extend_schema(summary='Деталка профиля сотрудника',
                      tags=['Сотрудники']),
)
class EmployeeUpdatedView(RetrieveUpdateAPIView):
    """Получение профиля сотрудника по id/изменение профиля сотрудника"""
    permission_classes = [IsAdminUser]
    queryset = User.objects.all()
    serializer_class = EmployeeUpdateRetrieveSerializer
    http_method_names = ('patch', 'get')

    def get_object(self):
        user_id = self.kwargs.get('user_id')
        return User.objects.get(id=user_id)

from drf_spectacular.utils import extend_schema_view, extend_schema
from rest_framework import generics
from rest_framework.generics import RetrieveUpdateAPIView

from users.serializers.api.employees import RegistrationEmployeeSerializer, \
    MeEmployeeSerializer, MeEmployeeUpdateSerializer
from django.contrib.auth import get_user_model

User = get_user_model()


@extend_schema_view(
    post=extend_schema(summary='Регистрация сотрудника',
                       tags=['Аутентификация & Авторизация: Сотрудники']),
)
class RegistrationEmployeeView(generics.CreateAPIView):
    """Регистрация сотрудника"""
    queryset = User.objects.all()
    # permission_classes = [AllowAny]
    serializer_class = RegistrationEmployeeSerializer


@extend_schema_view(
    get=extend_schema(summary='Профиль пользователя', tags=['Пользователи']),
    put=extend_schema(summary='Изменить профиль пользователя',
                      tags=['Пользователи']),
    patch=extend_schema(summary='Изменить частично профиль пользователя',
                        tags=['Пользователи']),
)
class MeEmployeeView(RetrieveUpdateAPIView):
    """Получение/обновления профиля сотрудника"""
    # permission_classes = [IsNotCorporate]
    queryset = User.objects.all()
    serializer_class = MeEmployeeSerializer
    http_method_names = ('get', 'patch')

    def get_serializer_class(self):
        if self.request.method in ['PUT', 'PATCH']:
            return MeEmployeeUpdateSerializer
        return MeEmployeeSerializer

    def get_object(self):
        return self.request.user

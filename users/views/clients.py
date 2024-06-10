from drf_spectacular.utils import extend_schema_view, extend_schema
from rest_framework import generics
from django.contrib.auth import get_user_model
from rest_framework.generics import RetrieveUpdateAPIView

from users.serializers.api.clients import RegistrationClientSerializer, \
    MeClientSerializer, MeClientUpdateSerializer

User = get_user_model()


@extend_schema_view(
    post=extend_schema(summary='Регистрация пользователя',
                       tags=['Аутентификация & Авторизация: Клиенты']),
)
class RegistrationClientView(generics.CreateAPIView):
    """Регистрация клиента"""
    queryset = User.objects.all()
    # permission_classes = [AllowAny]
    serializer_class = RegistrationClientSerializer


@extend_schema_view(
    get=extend_schema(summary='Профиль пользователя', tags=['Клиенты']),
    put=extend_schema(summary='Изменить профиль пользователя',
                      tags=['Клиенты']),
    patch=extend_schema(summary='Изменить частично профиль пользователя',
                        tags=['Клиенты']),
)
class MeClientView(RetrieveUpdateAPIView):
    """Получение/обновление профиля клиента"""
    # permission_classes = [IsNotCorporate]
    queryset = User.objects.all()
    serializer_class = MeClientSerializer
    http_method_names = ('get', 'patch')

    def get_serializer_class(self):
        if self.request.method in ['PUT', 'PATCH']:
            return MeClientUpdateSerializer
        return MeClientSerializer

    def get_object(self):
        return self.request.user

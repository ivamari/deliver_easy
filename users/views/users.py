from django.contrib.auth import get_user_model
from drf_spectacular.utils import extend_schema_view, extend_schema
from rest_framework import generics
from rest_framework.generics import RetrieveUpdateAPIView

from users.serializers.api.users import RegistrationUserSerializer

User = get_user_model()


@extend_schema_view(
    post=extend_schema(summary='Регистрация пользователя', tags=['Аутентификация & Авторизация']),
)
class RegistrationView(generics.CreateAPIView):
    queryset = User.objects.all()
    # permission_classes = [AllowAny]
    serializer_class = RegistrationUserSerializer


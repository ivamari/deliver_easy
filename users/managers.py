from django.contrib.auth.base_user import BaseUserManager
from rest_framework.exceptions import ParseError


class CustomUserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, phone_number=None, email=None, password=None,
                     **extra_fields):
        if not phone_number:
            raise ParseError('Укажите email или телефон')

        if email:
            email = self.normalize_email(email)

        user = self.model(email=email, phone_number=phone_number,
                          **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, phone_number=None, email=None, password=None,
                    **extra_fields):
        extra_fields.setdefault('is_superuser', False)
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_active', True)

        return self._create_user(phone_number, email, password,
                                 **extra_fields)

    def create_superuser(self, phone_number=None, email=None, password=None,
                         **extra_fields):
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_active', True)

        return self._create_user(phone_number, email, password,
                                 **extra_fields)

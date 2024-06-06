from django.contrib.auth.models import AbstractUser
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

from users.managers import CustomUserManager


class User(AbstractUser):
    username = None
    email = models.EmailField('Почта', unique=True, null=True, blank=True)
    phone_number = PhoneNumberField('Телефон', unique=True, null=True)
    USERNAME_FIELD = 'phone_number'

    is_corporate_account = models.BooleanField(
        'Корпоративный аккаунт', default=False)

    objects = CustomUserManager()

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    # # объект-свойство
    # @property
    # def full_name(self):
    #     return f'{self.first_name} {self.last_name}'

    def __str__(self):
        return str(self.phone_number)

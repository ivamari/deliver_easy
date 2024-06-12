from django.db import models
from cafes.models.cafes import Cafe
from django.contrib.auth import get_user_model

from cafes.models.positions import Position

User = get_user_model()


class Employee(models.Model):
    """Модель сотрудников кафе"""
    user = models.ForeignKey(User, models.CASCADE,
                             'cafes_info')
    cafe = models.ForeignKey(Cafe, models.CASCADE,
                             'employees_info', )
    position = models.ForeignKey(Position,
                                 models.CASCADE,
                                 'position_employees',
                                 verbose_name='Должность')

    class Meta:
        verbose_name = 'Сотрудник кафе'
        verbose_name_plural = 'Сотрудники кафе'

    def __str__(self):
        return f'Сотрудник {self.id} ({self.user} - {self.position})'

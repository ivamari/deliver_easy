from django.db import models

from cafes.models.cafes import Cafe
from django.contrib.auth import get_user_model

User = get_user_model()


class Department(models.Model):
    name = models.CharField('Название отдела', max_length=64)
    cafe = models.ManyToManyField(Cafe,
                                  verbose_name='Кафе',)
    manager = models.ForeignKey(User,
                                models.RESTRICT,
                                'departments_manager',
                                verbose_name='Менеджер',)

    class Meta:
        verbose_name = 'Отдел'
        verbose_name_plural = 'Отделы'
        ordering = ('name',)

    def __str__(self):
        return self.name


class Position(models.Model):
    name = models.CharField('Название должности', max_length=64)
    department = models.ForeignKey(Department, on_delete=models.CASCADE,
                                   verbose_name='Отдел')

    class Meta:
        verbose_name = 'Должность'
        verbose_name_plural = 'Должности'
        ordering = ('name', )




# class CafeEmployee(models.Model):
#     """Сотрудники кафе"""
#     cafe = models.ForeignKey(Cafe, models.CASCADE,
#                              'employees_info', )
#     user = models.ForeignKey(User, models.CASCADE,
#                              'cafes_info')
#     position = models.ForeignKey(Position,
#                                  )

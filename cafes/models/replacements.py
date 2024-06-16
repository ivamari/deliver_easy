from django.db import models

from cafes.models.employees import Employee
from cafes.models.departments import Department
from django.contrib.auth import get_user_model

from common.models.mixins import BaseDictModelMixin

User = get_user_model()


class ReplacementStatus(BaseDictModelMixin):
    """Статусы смены"""
    class Meta:
        verbose_name = 'Статус смены'
        verbose_name_plural = 'Статусы смены'


class Replacement(models.Model):
    """Смены"""
    department = models.ManyToManyField(Department, verbose_name='Отделы')
    time_start = models.DateTimeField('Дата и время начала смены')
    time_end = models.DateTimeField('Дата и время конца смены')

    class Meta:
        verbose_name = 'Смена'
        verbose_name_plural = 'Смены'

    def __str__(self):
        return f'{self.department}({self.time_start} - {self.time_end})'


class ReplacementMember(models.Model):
    """Сотрудники смены"""
    replacement = models.ManyToManyField(Replacement, verbose_name='Смены')
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE,
                                 related_name='employee_replacements')
    status = models.ForeignKey(ReplacementStatus, on_delete=models.RESTRICT,
                               verbose_name='Статус')

    class Meta:
        verbose_name = 'Участник смены'
        verbose_name_plural = 'Участники смены'

    def __str__(self):
        return f'{self.replacement} - {self.employee}'

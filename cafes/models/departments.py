from django.db import models
from cafes.models.cafes import Cafe
from django.contrib.auth import get_user_model

User = get_user_model()


class Department(models.Model):
    """Отделы"""
    cafe = models.ManyToManyField(Cafe,
                                  related_name='departments',
                                  verbose_name='Кафе', )
    name = models.CharField('Название отдела', max_length=64)
    manager = models.ForeignKey(User,
                                models.RESTRICT,
                                'departments_manager',
                                verbose_name='Менеджер', )
    members = models.ManyToManyField(User,
                                     'departments_members',
                                     verbose_name='Сотрудники отдела',
                                     blank=True, through='Member')

    class Meta:
        verbose_name = 'Отдел'
        verbose_name_plural = 'Отделы'
        ordering = ('name',)

    def __str__(self):
        return f'{self.name} ({self.id})'


class Member(models.Model):
    """Сотрудники отдела"""
    department = models.ForeignKey(Department, models.CASCADE,
                                   'members_info',
                                   )
    user = models.ForeignKey(User, models.CASCADE, 'groups_info')

    class Meta:
        verbose_name = 'Сотрудник отдела'
        verbose_name_plural = 'Сотрудники отделов'
        ordering = ('-date_joined',)
        unique_together = (('group', 'user'),)

    def __str__(self):
        return f'Employee {self.user}'

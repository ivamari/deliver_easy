from django.db import models

from cafes.models.cafes import Cafe
from cafes.models.departments import Department
from django.contrib.auth import get_user_model

User = get_user_model()


class CafeDepartment(models.Model):
    """Промежуточная модель кафе/отделы"""
    cafe = models.ForeignKey(Cafe,
                             related_name='cafe_departments',
                             on_delete=models.CASCADE)
    department = models.ForeignKey(Department,
                                   on_delete=models.CASCADE,
                                   related_name='cafe_departments',
                                   verbose_name='Название отдела', )
    manager = models.ForeignKey(User,
                                models.RESTRICT,
                                'departments_manager',
                                verbose_name='Менеджер',
                                blank=True,
                                null=True)
    members = models.ForeignKey(User,
                                on_delete=models.CASCADE,
                                related_name='departments_members',
                                verbose_name='Сотрудники отдела',
                                blank=True,
                                null=True,
                                )

    class Meta:
        verbose_name = 'Кафе/Отдел'
        verbose_name_plural = 'Кафе/Отделы'
        unique_together = (('department', 'manager', 'members'),)

    def __str__(self):
        return f'{self.department} ({self.id})'
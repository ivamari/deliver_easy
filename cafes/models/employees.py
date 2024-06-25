from django.db import models
from django.db.models.signals import m2m_changed, post_delete
from django.dispatch import receiver
from django.contrib.auth import get_user_model

from cafes.models.cafe_departments import CafeDepartment
from cafes.models.cafes import Cafe
from cafes.models.positions import Position


User = get_user_model()


class Employee(models.Model):
    """Сотрудники кафе"""
    user = models.ForeignKey(User, models.CASCADE,
                             'cafes_info')
    cafe = models.ForeignKey(Cafe, models.CASCADE,
                             'employees_info', )
    department = models.ForeignKey(CafeDepartment, models.CASCADE,
                                   related_name='employees_info', null=True,
                                   blank=True)
    position = models.ForeignKey(Position,
                                 models.CASCADE,
                                 'position_employees',
                                 verbose_name='Должность',
                                 null=True, blank=True)

    class Meta:
        verbose_name = 'Сотрудник кафе'
        verbose_name_plural = 'Сотрудники кафе'

    def __str__(self):
        return f'Сотрудник {self.id} ({self.user} - {self.position})'


@receiver(m2m_changed, sender=CafeDepartment.members.through)
def manage_employee_department_membership(sender, instance, action, reverse,
                                          pk_set, **kwargs):
    if action == "post_add":
        for user_id in pk_set:
            user = User.objects.get(pk=user_id)
            Employee.objects.get_or_create(
                user=user,
                cafe=instance.cafe,
                department=instance,
            )
    elif action == "post_remove":
        for user_id in pk_set:
            user = User.objects.get(pk=user_id)
            Employee.objects.filter(
                user=user,
                cafe=instance.cafe,
                department=instance
            ).delete()


@receiver(post_delete, sender=Employee)
def remove_employee_from_department(sender, instance, **kwargs):
    if instance.department:
        instance.department.members.remove(instance.user)

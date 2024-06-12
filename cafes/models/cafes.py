from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.gis.db import models as gis_models

from cafes.constants import OWNER_POSITION
from common.models.mixins import InfoMixin

User = get_user_model()


class Cafe(InfoMixin):
    """Модель кафе"""
    name = models.CharField('Название', max_length=64)
    owner = models.ForeignKey(User, models.RESTRICT,
                              'cafes_owners',
                              verbose_name='Владелец')
    location = gis_models.PointField(srid=4326, verbose_name='Локация')
    employees = models.ManyToManyField(User, 'cafes_employees',
                                       verbose_name='Сотрудники',
                                       blank=True,
                                       through='Employee')

    class Meta:
        verbose_name = 'Кафе'
        verbose_name_plural = 'Кафе'
        ordering = ('name',)

    def __str__(self):
        return f'{self.name} ({self.pk})'

    @property
    def owner_employee(self):
        obj, create = self.employees_info.get_or_create(
            position_id=OWNER_POSITION,
            defaults={'user': self.owner, }
        )
        return obj



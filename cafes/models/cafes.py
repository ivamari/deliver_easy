from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.gis.db import models as gis_models
User = get_user_model()


class Cafe(models.Model):
    name = models.CharField('Название', max_length=64)
    owner = models.ForeignKey(User, models.RESTRICT,
                              'cafes_owners',
                              verbose_name='Владелец')
    location = gis_models.PointField(srid=4326, verbose_name='Локация')

    class Meta:
        verbose_name = 'Кафе'
        verbose_name_plural = 'Кафе'
        ordering = ('name',)

    def __str__(self):
        return f'{self.name} ({self.id})'

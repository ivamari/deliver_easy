from django.db import models
from cafes.models.cafes import Cafe
from django.contrib.auth import get_user_model

User = get_user_model()


class Department(models.Model):
    name = models.CharField('Название отдела', max_length=64)
    cafe = models.ManyToManyField(Cafe,
                                  verbose_name='Кафе', )
    manager = models.ForeignKey(User,
                                models.RESTRICT,
                                'departments_manager',
                                verbose_name='Менеджер', )

    class Meta:
        verbose_name = 'Отдел'
        verbose_name_plural = 'Отделы'
        ordering = ('name',)

    def __str__(self):
        return f'{self.name} ({self.id})'




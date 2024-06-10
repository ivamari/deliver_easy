from django.db import models


class BaseDictModelMixin(models.Model):
    code = models.IntegerField('Код')
    name = models.CharField('Название', max_length=64)

    class Meta:
        abstract = True

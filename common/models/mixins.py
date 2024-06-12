from django.db import models
from django.utils import timezone
from django.contrib.auth import get_user_model

User = get_user_model()


class BaseDictModelMixin(models.Model):
    code = models.IntegerField('Код')
    name = models.CharField('Название', max_length=64)

    class Meta:
        abstract = True


class DateMixin(models.Model):
    created_at = models.DateTimeField('Created at', null=True, blank=True)
    updated_at = models.DateTimeField('Updated_at', null=True, blank=True)

    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        if not self.pk and not self.created_at:
            self.created_at = timezone.now()
        self.updated_at = timezone.now()
        return super(DateMixin, self).save(*args, **kwargs)


class InfoMixin(DateMixin):
    created_by = models.ForeignKey(User, models.SET_NULL,
                                   'CREATED_%(app_label)s_%(class)s',
                                   verbose_name='Created by', null=True)
    updated_by = models.ForeignKey(User, models.SET_NULL,
                                   'updated_%(app_label)s_%(class)s',
                                   verbose_name='Updated by', null=True)

    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        from crum import get_current_user

        user = get_current_user()
        if user and not user.pk:
            user = None
        if not self.pk:
            self.created_by = user

        self.updated_by = user
        super().save(*args, **kwargs)

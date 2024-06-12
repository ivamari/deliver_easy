import django_filters

from cafes.models.cafes import Cafe


class CafeFilter(django_filters.FilterSet):
    can_manage = django_filters.BooleanFilter('can_manage', label='Can manage')

    class Meta:
        model = Cafe
        fields = ('can_manage', 'id',)

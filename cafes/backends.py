from django.db.models import Q
from rest_framework.filters import BaseFilterBackend


class MyCafe(BaseFilterBackend):
    def filter_queryset(self, request, queryset, view):
        user = request.user
        return queryset.filter(
            Q(owner=user) | Q(employees=user)
        ).distinct()



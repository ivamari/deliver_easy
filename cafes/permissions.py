from rest_framework.permissions import BasePermission, SAFE_METHODS, \
    IsAuthenticated


class IsMyCafe(IsAuthenticated):
    def has_object_permission(self, request, view, obj):
        if obj.owner == request.user:
            return True

        if request.method in SAFE_METHODS:
            return request.user in obj.employees.all()

        return False

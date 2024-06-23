from rest_framework.permissions import IsAuthenticated, SAFE_METHODS


class IsMyCafe(IsAuthenticated):
    def has_object_permission(self, request, view, obj):
        # если запрос от директора организации
        if obj.owner == request.user:
            return True

        # если метод запроса безопасный
        if request.method in SAFE_METHODS:
            # то вернуть если запрашивает сотрудник организации
            return request.user in obj.employees.all()

        return False


class IsMyCafeDepartment(IsAuthenticated):
    def has_object_permission(self, request, view, obj):
        # если запрос от директора организации
        if obj.owner == request.user:
            return True
        return False


class IsMyDepartment(IsAuthenticated):
    def has_object_permission(self, request, view, obj):
        # если запрос от владельца кафе
        if obj.cafe.owner == request.user:
            return True

        # если метод запроса безопасный
        if request.method in SAFE_METHODS:
            return request.user in obj.cafe.employees.all()

        # если пользователь это менеджер отдела
        if obj.manager.user == request.user:
            return True
        return False


class IsMyCart(IsAuthenticated):
    def has_object_permission(self, request, view, obj):
        # если запрос от директора организации
        if obj.user == request.user:
            return True
        return False


class IsMyCafeEmployee(IsAuthenticated):
    def has_object_permission(self, request, view, obj):
        # если запрос от владельца кафе
        if obj.cafe.owner == request.user:
            return True

        # если метод запроса безопасный
        if request.method in SAFE_METHODS:
            return request.user in obj.cafe.employees.all()

        # если пользователь это менеджер отдела
        if obj.manager.user == request.user:
            return True
        return False

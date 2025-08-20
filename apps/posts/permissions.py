from rest_framework import permissions

class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    Позволяет редактировать объект только его автору.
    Все остальные пользователи имеют доступ только для чтения.
    """
    def has_object_permission(self, request, view, obj):
        # Разрешаем безопасные методы (GET, HEAD, OPTIONS) всем
        if request.method in permissions.SAFE_METHODS:
            return True
        # Разрешаем редактировать только автору объекта
        return obj.author == request.user

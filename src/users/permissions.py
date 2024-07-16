from rest_framework import permissions


class IsOwner(permissions.BasePermission):
    """
    Проверяет на то, что пользователь запрошивает информацию именно о себе.
    """
    def has_object_permission(self, request, view, obj) -> bool:
        return obj == request.user

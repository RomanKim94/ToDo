from rest_framework.permissions import BasePermission


class SelfOrAdminPersonPermission(BasePermission):

    def has_object_permission(self, request, view, obj):
        return bool(obj == request.user or request.user and request.user.is_staff is True)

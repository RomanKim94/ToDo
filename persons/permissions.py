from rest_framework.permissions import BasePermission


class SelfOrAdminPersonPermission(BasePermission):

    def has_object_permission(self, request, view, obj):
        return bool(obj.person == request.person or request.person and request.person.is_staff is True)

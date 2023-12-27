from rest_framework.permissions import BasePermission


class AdminOrOwnTaskPermission(BasePermission):

    def has_object_permission(self, request, view, obj):
        return bool(request.person and request.person.is_staff or request.person == obj.person)

    def has_permission(self, request, view):
        return bool(request.person and request.person.is_authenticated)

from rest_framework.permissions import BasePermission


class AdminOrOwnTaskPermission(BasePermission):

    def has_object_permission(self, request, view, obj):
        return bool(request.user and request.user.is_staff or request.user == obj.list.person)

    def has_permission(self, request, view):
        return bool(request.user and request.user.is_authenticated)

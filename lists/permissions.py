from rest_framework.permissions import BasePermission


class OwnListPermission(BasePermission):
    def has_object_permission(self, request, view, obj):
        return bool(request.person and obj.person == request.person)

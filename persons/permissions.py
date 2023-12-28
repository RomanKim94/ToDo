from rest_framework.permissions import BasePermission


class SelfOrAdminPersonPermission(BasePermission):

    def has_permission(self, request, view):
        return view.action in ['retrieve', 'create'] or request.user and request.user.is_staff

    def has_object_permission(self, request, view, obj):
        return bool(obj == request.user or request.user and request.user.is_staff)

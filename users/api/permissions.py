from rest_framework import permissions


class UserViewSetPermissions(permissions.BasePermission):
    """
    Permissions class for UserViewSet
    All can list, retrieve and create objects
    Only owners and staff can update and partial update
    Only staff users can destroy (delete) objects
    (users should set is_active to false)
    """
    # message = "Authentication credentials were not provided"

    def has_permission(self, request, view):
        return True

    def has_object_permission(self, request, view, obj):
        if view.action == 'destroy':
            return request.user and request.user.is_staff
        elif view.action in ('update', 'partial_update'):
            return obj.id == request.user.id or request.user.is_staff
        return True

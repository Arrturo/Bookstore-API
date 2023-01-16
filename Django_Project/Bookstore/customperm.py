from rest_framework import permissions


class IsCurrentUserOwnerOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        # SAFE_METHODS = Options. Head, Get
        if request.method in permissions.SAFE_METHODS:
            return True
        else:
            return obj.owner == request.user

class CurrentUserOwnerReadOnlyOrDenied(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.user.is_authenticated:
            return True

    def has_object_permission(self, request, view, obj):
        if obj.owner == request.user:
            if request.method in permissions.SAFE_METHODS:
                return True
            if request.request.user.is_superuser:
                return True

        return False
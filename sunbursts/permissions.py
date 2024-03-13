from rest_framework import permissions


class IsOwnerOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):

        # hover over SAFE_METHODS to see which qualify
        if request.method in permissions.SAFE_METHODS:
            return True

        if obj.owner is None:
            return True

        return obj.owner == request.user

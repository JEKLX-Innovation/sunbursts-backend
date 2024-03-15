"""
Module containing custom permission classes for REST framework.

Attributes:
    IsOwnerOrReadOnly: Custom permission class to allow only owners of objects to edit them.

Methods:
    has_object_permission(request, view, obj): Determines whether the user has permission to perform the action on the object.
"""
from rest_framework import permissions


class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    Custom permission class to allow only owners of objects to edit them.
    """
    def has_object_permission(self, request, view, obj):
        """
        Check if the user has permission to perform the action on the object.

        Args:
            request (HttpRequest): The incoming HTTP request.
            view (View): The view handling the request.
            obj (Any): The object being accessed.

        Returns:
            bool: True if the user has permission, False otherwise.
        """
        # hover over SAFE_METHODS to see which qualify
        if request.method in permissions.SAFE_METHODS:
            return True

        if obj.owner is None:
            return True

        return obj.owner == request.user

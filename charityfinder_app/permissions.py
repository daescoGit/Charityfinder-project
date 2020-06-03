from rest_framework import permissions


# extends base BasePermission

class IsAuthorOrReadOnly(permissions.BasePermission):
    # override has_object_permission
    # if in SAFE_METHODS = allow read
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True

        # write request - check/match true/false
        return obj.author == request.user


class IsOwnerOrAdmin(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS and request.user.is_staff:
            return True

        return obj.pk == request.user.pk

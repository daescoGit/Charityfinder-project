from rest_framework import permissions


# extends base BasePermission
class AllowRead(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True


class IsAuthorOrReadOnly(permissions.BasePermission):

    # override has_object_permission
    # if in SAFE_METHODS = allow read
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True

        # write request - check/match true/false
        return obj.author == request.user


class IsOwnerOrReadOnly(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.pk == request.user.pk


class IsLoggedOrReadOnly(permissions.BasePermission):

    pass

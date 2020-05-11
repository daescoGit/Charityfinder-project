from rest_framework import permissions


# extends base BasePermission
class IsAuthorOrReadOnly(permissions.BasePermission):

    # override has_object_permission, if in SAFE_METHODS = read only request
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True

        # else, write request - check/match true/false
        return obj.author == request.user

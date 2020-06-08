from rest_framework import permissions

class UpdateProfile(permissions.BasePermission):
    """Allow users to edit their own profile"""

    def has_object_permission(self, request, view, obj):
        """Check user is trying to edit their own profile."""

        #check if user request is in safe_method
        if request.method in permission.SAFE_METHODS:
            return True
        #check if user is authenticated
        return obj.id == request.user.id

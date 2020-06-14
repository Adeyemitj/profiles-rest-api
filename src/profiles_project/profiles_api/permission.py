from rest_framework import permissions

class UpdateProfile(permissions.BasePermission):
    """Allow users to edit their own profile"""

    def has_object_permission(self, request, view, obj):
        """Check user is trying to edit their own profile."""

        #check if user request is in safe_method
        if request.method in permissions.SAFE_METHODS:
            return True
        #check if user is authenticated
        return obj.id == request.user.id

# create a PostOwnStatus that inherit BasePermission from permissions
class PostOwnStatus(permissions.BasePermission):
    """Allow users to update their own status"""

    def has_object_permission(self, request, view, obj):
        """Check user is trying to update their own status"""

        # restrict non authenticated user editing profile 
        if request.method in permissions.SAFE_METHODS:
            return True

        #check if d user profile_id of the status id to be updated matches the request.user id
        return obj.user_profile.id == request.user.id

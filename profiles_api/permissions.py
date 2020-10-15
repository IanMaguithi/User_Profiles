from rest_framework import permissions


class UpdateOwnProfile(permissions.BasePermission):
    """Allow users to edit their own profile"""

    def has_object_permission(self, request, view, obj):
        """Check user is trying to edit their own profile"""

        if request.method in permissions.SAFE_METHODS:  # safe methods/ nondestructive include GET request
            return True

        return obj.id == request.user.id
        # returns True only if profile_id == user_id hence permission granted and false otherwise

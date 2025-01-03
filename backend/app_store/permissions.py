from rest_framework import permissions

class AllowBookAdd(permissions.BasePermission):
    """
    Custom permission to only allow read-only access for specific users.
    """

    def has_permission(self, request, view):

        # Allow safe methods (GET, HEAD, OPTIONS) for everyone
        if request.method in permissions.SAFE_METHODS:
            return True
        
        restricted_users = ['dholu', 'user2'] 
        if request.user.username in restricted_users:
            return False  # Disallow non-read methods (e.g., POST, PUT, DELETE)

        return True 

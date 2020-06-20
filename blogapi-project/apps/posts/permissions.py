from rest_framework import permissions


class IsAuthorOrReadOnly(permissions.BasePermission):

    """If a request
    contains HTTP verbs included in SAFE_METHODS –a tuple containing GET , OPTIONS , and
    HEAD –then it is a read-only request and permission is granted."""
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True

        """Otherwise the request is for a write of some kind, which means updating the API
        resource so either create, delete, or edit functionality. In that case, we check if the
        author of the object in question, which is our blog post obj.author matches the user
        making the request request.user ."""
        return obj.author == request.user

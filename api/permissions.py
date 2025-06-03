from rest_framework.permissions import BasePermission


class APIPermission(BasePermission):
    @staticmethod
    def is_safe(request):
        return request.method in ["GET", "HEAD", "OPTIONS"]


class AllowAny(APIPermission):
    def has_permission(self, request, view):
        return True


class IsAdmin(APIPermission):
    def has_permission(self, request, view):
        return request.user and getattr(request.user, "is_admin", False)


class IsAuthenticated(APIPermission):
    def has_permission(self, request, view):
        return request.user and request.user.is_authenticated


class IsAuthenticatedOrReadOnly(IsAuthenticated):
    def has_permission(self, request, view):
        if self.is_safe(request):
            return True
        return super().has_permission(request, view)


class IsOwner(APIPermission):
    def get_object_owner(self, obj):
        return getattr(obj, "owner", None)

    def has_object_permission(self, request, view, obj):
        owner = self.get_object_owner(obj)
        return owner and request.user and owner == request.user

from rest_framework.permissions import BasePermission


class IsEnterprise(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.role in ['ENTERPRISE', 'ADMIN']
    

class IsAdmin(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.role == 'ADMIN'

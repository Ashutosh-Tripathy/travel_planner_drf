from rest_framework.permissions import BasePermission, SAFE_METHODS
from rest_framework.permissions import IsAuthenticated

class IsAdminOrSelf(BasePermission):
    def s_object_permission(self, request, view, obj):
        return obj.owner == request.user or request.user.is_staff


class IsAdminOrManagerOrSelf(BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.owner == request.user or request.user.is_staff or request.user.role == 'manager'


class UserPermission(BasePermission):
    def has_permission(self, request, viewj):
       if request.method == 'POST':
           return True
       else: 
           return request.user and request.user.is_authenticated and ( request.user.is_staff or request.user.role == 'manager')


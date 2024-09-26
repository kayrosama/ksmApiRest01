from rest_framework.permissions import BasePermission

class IsAdminOrReadOnly(BasePermission):
    def has_permission(self, request, view):
        if request.nethod == "GET":
            return True
        else:
            return request.user.is_staff
        
        #return super().has_permission(request, view)
from rest_framework.permissions import BasePermission,SAFE_METHODS
class IsWorker(BasePermission):
    def has_permission(self,request,view):
        return request.user.role == 'worker'
    
class IsCustomer(BasePermission):
    def has_permission(self, request, view):
        return request.user.role == 'customer'
    
class IsAdmin(BasePermission):
    def has_permission(self,request,view):
        return request.user.role == 'admin' or request.user.is_staff
    
class IsOwnerOrRead(BasePermission):
    def has_permission(self, request, view):
        return request.method in SAFE_METHODS

    def has_object_permission(self,request,view,obj):
        if request.user.groups.filter(name='Workers').exists():
            return True
        return request.user == obj.user
    

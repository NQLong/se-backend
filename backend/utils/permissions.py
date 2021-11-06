from rest_framework.permissions import BasePermission
from utils import enums

class IsCustomerOnly(BasePermission):
    def has_permission(self, request, view):
        profile = request.user.profile
        return profile.type == enums.UserAccountType.CUSTOMER
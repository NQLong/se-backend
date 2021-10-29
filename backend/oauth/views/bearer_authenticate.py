from user_account.models.user import User
from rest_framework.permissions import IsAuthenticated, AllowAny
from ..validators import UserValidator
from utils.views import AbstractView, api_view

class BearerAuthenticateApi(AbstractView):

    @api_view(methods=['POST'],url_path='login',permissions=[AllowAny])
    def log_in(self, request, *args, **kwargs):
        validator = UserValidator(**(request.POST.dict() or request.data))
        identifier = validator.is_valid_for_log_in()

        user: User = User.objects.get(**identifier)

        device_token = user.generate_access_token()
        return {'access_token': device_token.key}


    @api_view(methods=['POST'],url_path='check_access_token')
    def check_access_token(self, request, *args, **kwargs):
        return None

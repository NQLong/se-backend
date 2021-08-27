from oauth.models import UserDeviceToken
from rest_framework.authentication import TokenAuthentication, get_authorization_header
from rest_framework.authtoken.models import Token
from . import exceptions, messages

class BearerTokenAuthentication(TokenAuthentication):
    keyword = 'bearer'

    def authenticate(self, request):
        auth_header = get_authorization_header(request=request)
        auth_header = auth_header.decode()
        auth_header = auth_header.split()

        if len(auth_header) <= 1:
            # Invalid token header. No credentials provided. Do not attempt to
            # authenticate.
            return None

        elif len(auth_header) > 2:
            # Invalid token header. The Token string should not contain spaces. Do
            # not attempt to authenticate.
            return None

        prefix = auth_header[0]
        token = auth_header[1]

        if prefix.lower() != self.keyword:
            return None


        if len(token) != 2:
            raise exceptions.AuthenticationException(messages.INVALID_OR_EXPIRED_TOKEN)
        
        user = self.get_authenticate_user(token[1])
        return user, token

    def get_authenticate_user(self, token):
        try:
            device_token = UserDeviceToken.objects.get(key=token)
        except Exception as exception:
            raise exceptions.AuthenticationException(messages.INVALID_OR_EXPIRED_TOKEN)

        device_token.validate()
        return device_token.user, device_token.key

from utils.models import AbstractModel
from django.db import models
from django.conf import settings
from utils.enums import DeviceType
from utils import messages, exceptions
from rest_framework.authtoken.models import Token
from datetime import datetime, timedelta

class UserDeviceToken(AbstractModel, Token):

    class Meta:
        unique_together = [['key', 'active']]

    user = models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='user_device_token_creator')
    key = models.TextField(null=True)
    device_type = models.CharField(max_length=16, choices= DeviceType.choices, default=DeviceType.WEBAPP,)
    client_ip = models.CharField(max_length=56)
    device_id = models.CharField(max_length=36, null=True, blank=True)
    device_token = models.CharField(max_length=163, null=True, blank=True)
    device_model = models.CharField(max_length=64, null=True, blank=True)
    user_agent = models.TextField(default='', null=True, blank=True)
    active = models.BooleanField(default=False)
    deactivated_at = models.DateTimeField(null=True, blank=True)

    @property
    def is_active(self):
        return self.active

    @classmethod
    def generate_key(cls):
        key = super().generate_key()
        while UserDeviceToken.objects.filter(key = key).exists():
            key = super().generate_key()
        return key

    def validate(self):
        created_at = self.created_at
        if created_at + timedelta(days=settings.TOKEN_LIFETIME) < datetime.now():
            raise exceptions.AuthenticationException(message=messages.INVALID_OR_EXPIRED_TOKEN)

    @classmethod
    def create(cls, *args, **kwargs):
        ...

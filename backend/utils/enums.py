from enum import unique
from django.db import models

@unique
class DeviceType(models.TextChoices):
    IOS = 'IOS'
    ANDROID = 'ANDROID'
    WEBAPP = 'WEBAPP'

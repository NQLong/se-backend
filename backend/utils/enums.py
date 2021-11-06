from enum import unique
from django.db import models

@unique
class DeviceType(models.TextChoices):
    IOS = 'IOS'
    ANDROID = 'ANDROID'
    WEBAPP = 'WEBAPP'

@unique
class UserAccountType(models.TextChoices):
    ADMIN = 'ADMIN'
    CUSTOMER = 'CUSTOMER'
    OWNER = 'OWNER'
    CLERK = 'CLERK'

@unique
class StorageType(models.TextChoices):
    INTERNAL = 'INTERNAL'
    S3 = 'S3'
    EXTERNAL = 'EXTERNAL'


@unique
class DirectoryFile(models.TextChoices):
    AVATAR = 'AVATAR'
    CHALLENGE = 'CHALLENGE'
    EVENT = 'EVENT'
    ARTICLE = 'ARTICLE'
    QUESTION = 'QUESTION'
    ANSWER = 'ANSWER'
    EMAIL = 'EMAIL'

@unique
class OrderStaus(models.TextChoices):
    REQUESTED = 'REQUEST'
    DENIED = 'DENIED'
    APPROVE = 'APPROVE'
    CANCEL = 'CANCEL'

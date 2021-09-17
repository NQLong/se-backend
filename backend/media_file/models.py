from django.db import models
from utils.models import AbstractModel
from user_account.models import User

class Media(AbstractModel):

    class Meta:
        db_table = 'media_file'

    filename = models.CharField(max_length=1024, null=False)
    description = models.TextField(null=True, blank=True)
    thumbnail = models.TextField(null=True, blank=True)
    thumbnail_size = models.BigIntegerField(null=True, blank=True)
    size = models.BigIntegerField(null=False)
    content_type = models.CharField(max_length=256, null=False)
    store_type = models.CharField(max_length=256, null=False)
    directory = models.TextField(null=True, blank=True)
    access_url = models.TextField(null=True, blank=True)
    deleted = models.BooleanField(null=False, default=False)
    digest = models.CharField(max_length=128, null=False)
    creator = models.ForeignKey(to=User, related_name='creator_media', on_delete=models.CASCADE, null=False)


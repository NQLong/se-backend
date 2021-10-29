import uuid
from django.db import models
from django.conf import settings
from django.core.validators import MinValueValidator
from utils import exceptions, messages

from utils.enums import StorageType, DirectoryFile



class Media(models.Model):

    uid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)

    file_name = models.CharField(max_length=1024, null=False, blank=False)

    description = models.TextField(null=True, blank=True)

    thumbnail = models.TextField(null=True, blank=True)
    thumbnail_size = models.IntegerField(null=False, blank=False, default=0)

    size = models.IntegerField(null=False, blank=False, default=0,
            validators=[MinValueValidator(0, 'size must be bigger than 0'), ],
        )

    storage_type = models.CharField(
        null=False,
        max_length=16,
        choices=StorageType.choices,
        default=StorageType.INTERNAL,
    )

    # TODO: Should validate when create media
    content_type = models.CharField(max_length=255, blank=False, null=False)

    directory = models.CharField(max_length=128, null=True, blank=True, choices=DirectoryFile.choices)

    access_url = models.TextField(blank=True, null=True)

    # file will be uploaded to MEDIA_ROOT/uploads
    file = models.FileField(upload_to='uploads/', blank=True, null=True)

    deleted = models.BooleanField(default=False)

    # Sometimes, we can not get digest of the file. (File from url for eg)
    digest = models.CharField(max_length=128, blank=True, null=True)

    creator = models.ForeignKey(
        null=False,
        to=settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='media_creator',
    )

    created_at = models.DateTimeField(auto_now=False, auto_now_add=True)
    updated_at = models.DateTimeField(
        auto_now=True, auto_now_add=False, null=True, blank=True)

    @property
    def media_url(self):
        '''
        If file from external resources -> use access_url
        If file from internal -> build a post-fix url - should append url host when get full url
        '''
        url = self.access_url
        host_url = settings.BASE_MEDIA_HOST
        if self.file:
            url = f'{host_url}{settings.MEDIA_URL}{self.file}'
        return url

    def __str__(self) -> str:
        return f'{self.file_name} - {self.media_url}'

    def to_json(self):
        return {
            "uid": self.uid,
            "file_name": self.file_name,
            "description": self.description,
            "size": self.size,
            "content_type": self.content_type,
            "media_url": self.media_url,
        }

    @staticmethod
    def get(uid=None):
        try:
            return Media.objects.get(uid=uid)
        except Exception as exc:
            raise exceptions.ValidationException(
                message=messages.NOT_FOUND_MEDIA
            )

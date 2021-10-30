from django.db import models
import uuid
import binascii
import os
from django.utils.text import slugify
# Create your models here.
class AbstractModel(models.Model):
    class Meta:
        abstract = True

    uid = models.UUIDField(null=False, editable=False, default=uuid.uuid4, unique=True)
    created_at = models.DateTimeField(auto_now=False, auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, auto_now_add=False)


def generate_random_token(length = 5):
    return binascii.hexlify(os.urandom(length)).decode()

def generate_unique_slug_field(model, source, field):
    _slug = slugify(source)
    slug = _slug
    if model.objects.filter(**{field:_slug}).exists():
        for i in range(1,10):
            slug = f'{_slug}-{generate_random_token(i)}'
            if not model.objects.filter(**{field:slug}).exists():
                break
    return slug

from django.db import models
import uuid
# Create your models here.
class AbstractModel(models.Model):
    class Meta:
        abstract = True

    uid = models.UUIDField(null=False, editable=False, default=uuid.uuid4, unique=True)
    created_at = models.DateTimeField(auto_now=False, auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, auto_now_add=False)

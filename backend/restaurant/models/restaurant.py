from django.db import models
from utils.models import AbstractModel
from user_account.models import User


class Restaurant(AbstractModel):
	class Meta:
		db_table = 'restaurant'
	name = models.TextField(null=False)
	address = models.TextField(null=False)
	hot_line = models.CharField(max_length=16, null=True, blank=True)
	open_at = models.DateTimeField(null=False)
	close_at = models.DateTimeField(null=False)
	creator = models.ForeignKey(to=User, related_name='creator_restaurant', on_delete=models.CASCADE, null=False)


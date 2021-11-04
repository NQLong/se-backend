from django.db import models
from django.db.models.fields import related
from utils.models import AbstractModel
from user_account.models import User
from restaurant.models import Restaurant
from media_file.models import Media
from autoslug import AutoSlugField

class Menu(AbstractModel):

	class Meta:
		db_table = 'menu'

	title = models.CharField(null=False, max_length=1024)
	code = AutoSlugField(populate_from='title', unique=True)
	active = models.BooleanField(default=False, null=False)
	image = models.ForeignKey(to=Media, related_name='image_menu', on_delete=models.CASCADE, null=True, blank=True)
	restaurant = models.ForeignKey(to=Restaurant, related_name='restaurant_menu', on_delete=models.CASCADE)
	description = models.TextField(null=True, blank=True)
	creator = models.ForeignKey(to=User, related_name='creator_menu', on_delete=models.CASCADE, null=True, blank=True)
	ordinal = models.IntegerField(null=False)

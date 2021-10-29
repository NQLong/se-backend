from django.db import models
from django.db.models.fields import related
from utils.models import AbstractModel
from user_account.models import User
from restaurant.models import Restaurant
from media_file.models import Media

class Menu(AbstractModel):

	class Meta:
		db_table = 'menu'
	image=models.ForeignKey(to=Media,related_name='image_menu',on_delete=models.CASCADE,null=False)
	restaurant = models.ForeignKey(to=Restaurant, related_name='restaurant_menu', null=False, on_delete=models.CASCADE)
	description=models.TextField(null=True, blank=True)
	creator=models.ForeignKey(to=User,related_name='creator_menu',on_delete=models.CASCADE,null=False)
	ordinal=models.IntegerField(null=False)

from django.db import models
from utils.models import AbstractModel
from user_account.models import User
from restaurant.models.dish import Dish
from media_file.models import Media
class Menu(models.Model):

        class Meta:
                db_table = 'menu'
        dish=models.ForeignKey(to=Dish,related_name='dish_menu',on_delete=models.CASCADE,null=False)
        image=models.ForeignKey(to=Media,related_name='image_menu',on_delete=models.CASCADE,null=False)
        creator=models.ForeignKey(to=User,related_name='creator_menu',on_delete=models.CASCADE,null=False)
        
        ordinal=models.IntegerField(null=False)
        description=models.TextField(null=False)
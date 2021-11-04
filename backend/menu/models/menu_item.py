from django.db import models
from utils.models import AbstractModel
from user_account.models import User
from restaurant.models.dish import Dish
from menu.models.menu import Menu
from autoslug import AutoSlugField

class MenuItem(AbstractModel):
    class Meta:
        db_table = 'menu_item'
        unique_together = [['menu', 'dish']]
    
    dish=models.ForeignKey(to=Dish,related_name='dish_menu_item',on_delete=models.CASCADE,null=False)
    menu=models.ForeignKey(to=Menu,related_name='menu_menu_item',on_delete=models.CASCADE,null=False)
    unit_price=models.TextField(null=False)
    ordinal=models.IntegerField(null=False)
    active=models.BooleanField(null=False, default=True)
    creator=models.ForeignKey(to=User,related_name='creator_menu_item',on_delete=models.CASCADE,null=False)

from django.db import models
from utils.models import AbstractModel
from user_account.models import User
from restaurant.models.dish import Dish
from menu.models.menu import Menu
class MenuItem(models.Model):
    class Meta:
        db_table = 'menu'
    
    dish=models.ForeignKey(to=Dish,related_name='dish_menu',on_delete=models.CASCADE,null=False)
    creator=models.ForeignKey(to=User,related_name='creator_menu',on_delete=models.CASCADE,null=False)
    ordinal=models.IntegerField(null=False)
    
    unit_price=models.TextField(null=False)
    menu=models.ForeignKey(to=Menu,related_name='menu_menu_item',on_delete=models.CASCADE,null=False)
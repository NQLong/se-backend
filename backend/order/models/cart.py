from user_account.models.user import User
from utils.models import AbstractModel
from restaurant.models import Restaurant
from django.db import models
from menu.models import MenuItem


class Cart(AbstractModel):
    class Meta:
        db_table = 'cart'

    restaurant = models.ForeignKey(to=Restaurant, related_name='restaurant_cart', on_delete=models.CASCADE)
    user = models.ForeignKey(to=User, related_name='user_cart', on_delete=models.CASCADE)

class CartItem(AbstractModel):
    class Meta:
        db_table = 'cart_item'

    cart = models.ForeignKey(
        to=Cart, related_name='cart_cart_item', on_delete=models.CASCADE)
    menu_item = models.ForeignKey(
        to=MenuItem, related_name='menu_item_cart_item', on_delete=models.CASCADE)
    notes = models.TextField(null=True, blank=True)
    quantity = models.IntegerField(null=False, default=1)
    deleted = models.BooleanField(null=False, default=False)

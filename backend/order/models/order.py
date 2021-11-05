from utils import enums
from user_account.models.user import User
from utils.models import AbstractModel
from restaurant.models import Restaurant
from django.db import models
from menu.models import MenuItem


class Order(AbstractModel):
    class Meta:
        db_table = 'order'


    user = models.ForeignKey(to=User, related_name='user_order', on_delete=models.CASCADE)
    restaurant = models.ForeignKey(to=Restaurant, related_name='restaurant_order', on_delete=models.CASCADE)
    stauts = models.CharField(max_length=512, choices=enums.OrderStaus.choices, default=enums.OrderStaus.REQUESTED)


class OrderItem(AbstractModel):
    class Meta:
        db_table = 'order_item'

    order = models.ForeignKey(
        to=Order, related_name='order_order_item', on_delete=models.CASCADE)
    notes = models.TextField(null=True, blank=True)
    dish = models.ForeignKey(
        to=MenuItem, related_name='dish_order_item', on_delete=models.CASCADE)
    quantity = models.IntegerField(null=False, default=1)
    unit_price = models.FloatField(null=False)

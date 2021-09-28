from django.db import models
from utils.models import AbstractModel
from user_account.models import User
from restaurant.models.restaurant import Restaurant
class Dish(AbstractModel):
    class Meta:
        db_table = 'dish'
    name = models.CharField(max_length=1024, null=False)
    description = models.TextField(null=True, blank=True)
    restaurant = models.ForeignKey(to=Restaurant, related_name='restaurant_dish', on_delete=models.CASCADE, null=False)
    served = models.IntegerField(null=False)
    creator = models.ForeignKey(to=User, related_name='creator_dish', on_delete=models.CASCADE, null=False)

from django.db import models
from django.db.models.fields import IntegerField
from utils.models import AbstractModel
from user_account.models import User
from restaurant.models.restaurant import Restaurant

class Table(AbstractModel):
    class Meta:
        db_table = 'table'
    ordinal = models.IntegerField(null=False)
    restaurant = models.ForeignKey(to=Restaurant, related_name='restaurant_table', on_delete=models.CASCADE, null=False)
    description = models.TextField(null=True, blank=True)
    creator = models.ForeignKey(to=User, related_name='creator_table', on_delete=models.CASCADE, null=False)
    status = models.CharField(max_length=32, null=False)
    capacity = models.IntegerField(null=False)

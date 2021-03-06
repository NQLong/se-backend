from django.db import models
from utils.models import AbstractModel
from user_account.models import User
from restaurant.models.dish import Dish
from media_file.models import Media
class DishBanner(AbstractModel):
    class Meta:
        db_table = 'dish_banner'
    image = models.ForeignKey(to=Media, related_name='image_dish_banner', on_delete=models.CASCADE, null=False)
    dish = models.ForeignKey(to=Dish, related_name='dish_dish_banner', on_delete=models.CASCADE, null=False)
    description = models.TextField(null=True, blank=True)
    ordinal = models.IntegerField(null=False)
    creator = models.ForeignKey(to=User, related_name='creator_dish_banner', on_delete=models.CASCADE, null=False)

from django.db import models
from utils.models import AbstractModel
from user_account.models import User
from media_file.models import Media
from restaurant.models import Restaurant
class  RestaurantBanner(AbstractModel):
    class Meta:
        db_table = 'restaurant_banner'
    image = models.ForeignKey(to=Media, related_name='image_restaurant_banner', on_delete=models.CASCADE, null=False)
    restaurant = models.ForeignKey(to=Restaurant, related_name='restaurant_restaurant_banner', on_delete=models.CASCADE, null=False)
    description = models.TextField(null=True, blank=True)
    creator = models.ForeignKey(to=User, related_name='creator_restaurant_banner', on_delete=models.CASCADE, null=False)
    ordinal = models.IntegerField(null=False)


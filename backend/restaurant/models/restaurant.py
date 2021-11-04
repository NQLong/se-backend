from django.db import models
from django.db.models.query import QuerySet
from django.db.models.query_utils import Q
from media_file.models import Media
from utils import exceptions, messages
from utils.exceptions import NotFoundException
from utils.models import AbstractModel
from user_account.models import User
from autoslug import AutoSlugField


class Restaurant(AbstractModel):
    class Meta:
        db_table = 'restaurant'
    code = AutoSlugField(populate_from='title', unique=True)
    name = models.TextField(null=False)
    address = models.TextField(null=False)
    hot_line = models.CharField(max_length=16, null=True, blank=True)
    open_at = models.TimeField(null=False)
    close_at = models.TimeField(null=False)
    creator = models.ForeignKey(to=User, related_name='creator_restaurant', on_delete=models.CASCADE, null=False)


    @staticmethod
    def create_from_dict(data: dict):
        restaurant = Restaurant.objects.create(**data)
        return Restaurant.get(restaurant.uid)

    @staticmethod
    def get(uid=None, code=None, query: QuerySet=None):
        try:
            query = query or Restaurant.objects.all()
            query = query.prefetch_related('restaurant_restaurant_banner')
            return query.get(
                Q(uid=uid) if uid else Q(code=code)
            )
        except Exception as exception:
            raise exceptions.ValidationException(message=messages.NOT_FOUND_RESTAURANT)

    def update_banner(self, media_uid_list: list, user: User):
        from restaurant.models import RestaurantBanner
        new_banners = [RestaurantBanner(
            restaurant=self,
            image=Media.get(uid=media_uid),
            ordinal=ordinal,
            creator=user
        ) for ordinal, media_uid in enumerate(media_uid_list)]
        new_banners = RestaurantBanner.objects.bulk_create(new_banners)
        return new_banners



from django.db import models
from django.db.models.query import QuerySet
from django.db.models.query_utils import Q
from media_file.models import Media
from utils import exceptions, messages
from utils.models import AbstractModel
from user_account.models import User
from restaurant.models.restaurant import Restaurant
from utils.models import generate_unique_slug_field
from autoslug import AutoSlugField
class Dish(AbstractModel):
    class Meta:
        db_table = 'dish'

    code = AutoSlugField(populate_from='title', unique=True)
    name = models.CharField(max_length=1024, null=False)
    description = models.TextField(null=True, blank=True)
    restaurant = models.ForeignKey(to=Restaurant, related_name='restaurant_dish', on_delete=models.CASCADE, null=False)
    serve_count = models.IntegerField(null=False, default=0)
    creator = models.ForeignKey(to=User, related_name='creator_dish', on_delete=models.CASCADE, null=False)

    def save(self, *args, **kwargs):
        if not self.code:
            self.code = generate_unique_slug_field(
                model=Dish,
                source=self.name,
                field='code',
            )
        super().save(*args,**kwargs)

    @staticmethod
    def create_from_dict(data:dict):
        dish = Dish.objects.create(
            name=data.get('name', None),
            description=data.get('description', None),
            restaurant=data.get('restaurant', None),
            creator=data.get('creator', None),
        )
        return {"code": dish.code}, dish

    @staticmethod
    def get(uid=None, code=None, query: QuerySet=None):
        try:
            query = query or Dish.objects.all()
            query = query.prefetch_related('dish_dish_banner', 'dish_dish_banner__image')
            return query.get(
                Q(uid=uid) if uid else Q(code=code)
            )
        except Exception as exception:
            raise exceptions.ValidationException(message=messages.NOT_FOUND_DISH)

    def update_banner(self, media_uid_list: list, user: User):
        from restaurant.models import DishBanner
        new_banners = [DishBanner(
            dish=self,
            image=Media.get(uid=media_uid),
            ordinal=ordinal,
            creator=user
        ) for ordinal, media_uid in enumerate(media_uid_list)]
        new_banners = DishBanner.objects.bulk_create(new_banners)
        return new_banners


class Category(AbstractModel):
    title = models.CharField(max_length=1024, unique=True)
    code = AutoSlugField(populate_from='title', unique=True)


class DishCategory(AbstractModel):
    dish = models.ForeignKey(to=Dish, related_name='dish_category_dish', on_delete=models.CASCADE, null=False)
    category = models.ForeignKey(to=Category, related_name='dish_category_category', on_delete=models.CASCADE, null=False)


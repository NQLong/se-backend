from django.db.models.query_utils import Q
from restaurant.models.dish import Category, Dish, DishCategory
from restaurant.models.restaurant import Restaurant
from restaurant.serializers.dish import DishListSerializer, DishSerializer
from restaurant.validators.dish import DishValidator
from utils.views import api_view, AbstractView
from rest_framework import permissions

class DishApi(AbstractView):
    permission_classes = [permissions.IsAuthenticated]

    @api_view(
        methods=['POST'],
        url_path='create',
    )
    def create_dish(self, request, *args, **kwargs):
        data = request.data
        validator = DishValidator(**data)
        dish_data = validator.is_valid_for_create(request.user)
        new_dish_identifier, new_dish = Dish.create_from_dict(dish_data)
        banners = data.get('banners', [])
        new_dish.update_banner(banners, request.user)
        dish = Dish.get(**new_dish_identifier)
        serializer = DishSerializer(dish)
        return serializer.data



    @api_view(
        methods=['GET'],
        url_path='get',
        permissions=[permissions.AllowAny]
    )
    def get_dish(self, request, *args, **kwargs):
        data = request.GET.dict()
        validator = DishValidator(**data)
        identifier = validator.is_valid_for_get()
        restaurant = Dish.get(**identifier)
        serializer = DishSerializer(restaurant)
        return serializer.data


    @api_view(
        methods=['POST'],
        url_path='matrix',
        permissions=[permissions.AllowAny],
        paginate=True,
    )
    def get_dish(self, request, *args, **kwargs):
        serializer = DishSerializer(Dish.objects.filter(restaurant=request.user.profile.restaurant), many=True)
        return serializer.data

    @api_view(
        methods=['POST'],
        url_path='add-category',
    )
    def add_category(self, request):
        data = request.data
        dish_uid = data.get('dish_uid')
        dish_code = data.get('dish_code')
        dish = Dish.get(uid=dish_uid, code=dish_code)
        categories_data = data.get('categories')
        categories = Category.objects.filter(
            Q(uid__in=categories_data) |
            Q(code__in=categories_data)
        )
        DishCategory.objects.filter(
            dish=dish,
            category__in=categories
        ).delete()
        DishCategory.objects.bulk_create(
            [
                DishCategory(
                    dish=dish,
                    category=category
                ) for category in categories
            ]
        )
        return


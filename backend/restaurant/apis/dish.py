# from restaurant.models.dish import Dish
# from restaurant.validators.dish import DishValidator
# from utils.views import api_view, AbstractView
# from rest_framework import permissions

# class RestaurantApi(AbstractView):
#     permission_classes = [permissions.IsAuthenticated]

#     @api_view(methods=['POST'], url_path='create')
#     def create_dish(self, request, *args, **kwargs):
#         data = request.data
#         validator = DishValidator(data)
#         data = validator.is_valid_for_create(request.user)
#         dish: Dish = Dish.create_from_dict(data)

#         banners = data.get('banners', [])
#         dish.update_banner(banners)
#         serializer = DishSerializer(restaurant)
#         return serializer.data

#     # @api_view(
#     #     methods=['GET'],
#     #     url_path='get',
#     #     permissions=[permissions.AllowAny]
#     # )
#     # def get_restaurant(self, request, *args, **kwargs):
#     #     data = request.GET.dict()
#     #     validator = RestaurantValidator(data)
#     #     identifier = validator.is_valid_for_get()
#     #     restaurant = Restaurant.get(**identifier)
#     #     serializer = RestaurantSerializer(restaurant)
#     #     return serializer.data





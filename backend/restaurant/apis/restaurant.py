from rest_framework.decorators import parser_classes
from restaurant.models.restaurant import Restaurant
from restaurant.serializers.restaurant import RestaurantSerializer
from restaurant.validators.restaurant import RestaurantValidator
from utils.views import api_view, AbstractView
from rest_framework import permissions, parsers

class RestaurantApi(AbstractView):
    permission_classes = [permissions.IsAuthenticated]

    @api_view(
        methods=['POST'], 
        url_path='create', 
        permissions=[permissions.IsAdminUser],
        exception_handler=False,
    )
    def create_restaurant(self, request, *args, **kwargs):
        request_data = request.data
        validator = RestaurantValidator(**request_data)
        data = validator.is_valid_for_create(request.user)
        restaurant: Restaurant = Restaurant.create_from_dict(data)

        banners = request_data.get('banners', [])
        restaurant.update_banner(banners, request.user)
        restaurant = Restaurant.objects.get(uid=restaurant.uid)
        serializer = RestaurantSerializer(restaurant)
        return serializer.data

    @api_view(
        methods=['GET'], 
        url_path='get', 
        permissions=[permissions.AllowAny]
    )
    def get_restaurant(self, request, *args, **kwargs):
        data = request.GET.dict()
        validator = RestaurantValidator(**data)
        identifier = validator.is_valid_for_get()
        restaurant = Restaurant.get(**identifier)
        serializer = RestaurantSerializer(restaurant)
        return serializer.data

    @api_view(
        methods=['POST'], 
        url_path='matrix', 
        permissions=[permissions.AllowAny],
        paginate=True,
    )
    def matrix_restaurant(self, request, *args, **kwargs):
        data = request.POST.dict()
        # validator = RestaurantValidator(**data)
        # identifier = validator.is_valid_for_get()
        # restaurant = Restaurant.get(**identifier)
        restaurants = Restaurant.objects.all()
        serializer = RestaurantSerializer(restaurants, many=True)
        return serializer.data



from restaurant.models.dish import Category, Dish
from restaurant.serializers.dish import CategorySerializer, DishListSerializer, DishSerializer
from restaurant.validators.dish import DishValidator
from utils.views import api_view, AbstractView
from rest_framework import permissions

class CategoryApi(AbstractView):
    permission_classes = [permissions.IsAuthenticated]

    @api_view(
        methods=['GET'],
        url_path='matrix',
        paginate=True
    )
    def matrix_category(self, request, *args, **kwargs):
        query = Category.objects.all()
        data = CategorySerializer(query, many=True).data
        return data

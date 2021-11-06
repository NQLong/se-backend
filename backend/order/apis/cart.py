from utils.views import AbstractView, api_view
from rest_framework.permissions import IsAuthenticated
from utils import enums
from restaurant.models import Restaurant
from order.models import Cart

class CartApi(AbstractView):
    permission_classes = (IsAuthenticated,)
    @api_view(
        methods=['GET'],
        url_path='get',
    )
    def get_cart(self, request):
        data=request.GET.dict()
        user_type = request.user.profile.type
        if user_type == enums.UserAccountType.CUSTOMER:
            restaurant_uid = data.get('restaurant_uid', None)
            restaurant_code = data.get('restaurant_code', None)
            restaurant = Restaurant.get(uid=restaurant_uid, code=restaurant_code)
        else:
            restaurant = request.user.profile.restaurant
        cart, created = Cart.objects.get_or_create(
            restaurant=restaurant,
            customer=request.user
        )

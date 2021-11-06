from utils.views import AbstractView, api_view
from rest_framework.permissions import IsAuthenticated
from utils import enums, exceptions, messages
from restaurant.models import Restaurant
from order.models import CartItem, Cart
from menu.models import MenuItem
from order.serializers import CartItemSerializer


class CartApi(AbstractView):
    permission_classes = (IsAuthenticated,)
    
    @api_view(
        methods=['GET'],
        url_path='get',
    )
    def get_cart_item(self, request):
        data=request.GET.dict()
        cart_item_uid = data.get('menu_item_uid', None)
        cart_item = CartItem.objects.get(uid=cart_item_uid)
        user = cart_item.cart.user
        if user != request.user:
            raise exceptions.PermissionDenied(messages.NO_PERMISSION)
        return CartItemSerializer(cart_item).data

    @api_view(
        methods=['POST'],
        url_path='create',
    )
    def create_cart_item(self, request):
        data=request.data
        cart_uid = data.get('cart_uid', None)
        menu_item_uid = data.get('menu_item_uid', None)
        quantity = data.get('quantity', None)
        if not cart_uid or not menu_item_uid or not quantity:
            raise exceptions.BadRequest(messages.MISSING_PARAMETERS)
        cart = Cart.objects.get(uid=cart_uid)
        menu_item = MenuItem.objects.get(uid=menu_item_uid)
        if cart.user != request.user:
            raise exceptions.PermissionDenied(messages.NO_PERMISSION)
        if menu_item.restaurant != cart.restaurant:
            raise exceptions.PermissionDenied(messages.NO_PERMISSION)
        if menu_item.quantity < quantity:
            raise exceptions.BadRequest(messages.INSUFFICIENT_QUANTITY)
        cart_item = CartItem.objects.create(
            cart=cart,
            menu_item=menu_item,
            quantity=quantity,
        )
        return CartItemSerializer(cart_item).data

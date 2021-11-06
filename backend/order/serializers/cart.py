from rest_framework import serializers
from order.models import Cart
from menu.serializers import MenuItemSerializer
from order.models.cart import CartItem

class CartItemSerializer(serializers.ModelSerializer):
    menu_item = MenuItemSerializer(read_only=True)
    
    class Meta:
        model = Cart
        fields = '__all__'

class CartSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Cart
        fields = '__all__'

    def to_representation(self, instance):
        cart_items = instance.cart_cart_item.all()
        cart_items = cart_items.filter(deleted=False)
        cart_items_data = CartItemSerializer(cart_items, many=True).data
        data = super().to_representation(instance)
        data['cart_items'] = cart_items_data
        return data
from rest_framework import serializers
from menu.models import MenuItem
from restaurant.serializers import DishListSerializer

class MenuItemSerializer(serializers.ModelSerializer):
    dish = DishListSerializer()

    class Meta:
        model = MenuItem
        fields = '__all__'

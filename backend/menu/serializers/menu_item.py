from rest_framework import serializers
from menu.models import MenuItem
from restaurant.serializers import DishSerializer

class MenuItemSerializer(serializers.ModelSerializer):
    dish = DishSerializer()

    class Meta:
        model = MenuItem
        fields = '__all__'

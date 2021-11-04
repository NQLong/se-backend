from rest_framework import serializers
from menu.models import Menu
from menu.serializers.menu_item import MenuItemSerializer

class MenuListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Menu
        fields = '__all__'

class MenuSerializer(serializers.ModelSerializer):
    menu_items = MenuItemSerializer(source='menu_menu_item', many=True)
    class Meta:
        model = Menu
        fields = '__all__'

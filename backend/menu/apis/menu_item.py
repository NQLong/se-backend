from menu.filters.menu_item import MenuItemFilter
from menu.models.menu_item import MenuItem
from menu.serializers.menu_item import MenuItemSerializer
from utils.views import api_view, AbstractView
from rest_framework import permissions
from menu.models import Menu
from django.db.models import Q
from menu.serializers import *
from menu.filters import *

class MenuItemApi(AbstractView):
    permission_classes = [permissions.IsAuthenticated]

    @api_view(
        methods=['GET'],
        url_path='get',
        permissions=[permissions.AllowAny]
    )
    def get_menu_item(self, request):
        data = request.GET.dict()
        menu_uid = data.get('menu_item_uid')
        menu_code = data.get('menu_item_code')
        menu_item = MenuItem.objects.get(
            Q(uid=menu_uid) |
            Q(code=menu_code)
        )
        serializer = MenuItemSerializer(menu_item)
        return serializer.data

    @api_view(
        methods=['POST'],
        url_path='matrix',
        permissions=[permissions.AllowAny],
        paginate=True
    )
    def list_menu_item(self, request):
        data = request.data
        query_param = Q(active=True)
        if request.user:
            query_param = query_param | Q(menu__restaurant=request.user.profile.restaurant)

        query = MenuItem.objects.filter(query_param)
        query = MenuItemFilter(data=data, queryset=query).qs
        serializer = MenuItemSerializer(query, many=True)
        return serializer.data



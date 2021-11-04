from utils.views import api_view, AbstractView
from rest_framework import permissions
from menu.models import Menu
from django.db.models import Q
from menu.serializers import *
from menu.filters import *

class MenuApi(AbstractView):
    permission_classes = [permissions.IsAuthenticated]

    @api_view(
        methods=['GET'],
        url_path='get',
    )
    def get_menu(self, request):
        data = request.GET.dict()
        menu_uid = data.get('menu_uid')
        menu_code = data.get('menu_code')
        menu = Menu.objects.get(
            Q(uid=menu_uid) |
            Q(code=menu_code)
        )
        serializer = MenuSerializer(menu)
        return serializer.data

    @api_view(
        methods=['POST'],
        url_path='matrix',
        
    )
    def list_menu(self, request):
        data = request.data
        query = Menu.objects.filter(
            Q(active=True) |
            Q(restaurant=request.user.profile.restaurant)
        )
        query = MenuFilter(data=data, queryset=query).qs
        serializer = MenuListSerializer(query, many=True)
        return serializer.data



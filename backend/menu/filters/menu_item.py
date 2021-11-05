from django_filters import FilterSet
import django_filters
from menu.models import MenuItem

class MenuItemFilter(FilterSet):
    menu_uid = django_filters.CharFilter('menu__uid', 'exact')
    menu_code = django_filters.CharFilter('menu__code', 'exact')
    restaurant_code = django_filters.CharFilter('menu__restaurant__code', 'exact')
    restaurant_uid = django_filters.CharFilter('menu__restaurant__uid', 'exact')
    dish_name = django_filters.CharFilter('dish__name', 'icontains')

    class Meta:
        model = MenuItem
        fields = [
            'uid',
            'dish',
            'active'
        ]
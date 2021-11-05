from django_filters import FilterSet
import django_filters
from menu.models import Menu

class MenuFilter(FilterSet):
    menu_uid = django_filters.CharFilter('uid', 'exact')
    menu_code = django_filters.CharFilter('code', 'exact')
    restaurant_code = django_filters.CharFilter('restaurant__code', 'exact')
    restaurant_uid = django_filters.CharFilter('restaurant__uid', 'exact')

    class Meta:
        model = Menu
        fields = [
            'uid',
            'title',
            'code',
            'restaurant',
            'active'
        ]
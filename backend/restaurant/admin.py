from django.contrib import admin
from restaurant.models import Restaurant,RestaurantBanner,DishBanner,Dish,Table

# Register your models here.
admin.site.register(Restaurant)
admin.site.register(RestaurantBanner)

admin.site.register(Dish)
admin.site.register(DishBanner)

admin.site.register(Table)
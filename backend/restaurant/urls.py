from rest_framework import routers
from .apis import RestaurantApi, DishApi

router = routers.DefaultRouter(trailing_slash=False)
router.register('restaurants', RestaurantApi, basename='restaurants')
router.register('restaurants/dishes', DishApi, basename='dishes')

urlpatterns = router.urls

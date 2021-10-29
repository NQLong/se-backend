from rest_framework import routers
from .apis import RestaurantApi

router = routers.DefaultRouter(trailing_slash=False)
router.register('restaurants', RestaurantApi, basename='restaurants')

urlpatterns = router.urls

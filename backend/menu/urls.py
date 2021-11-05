from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .apis import *

router = DefaultRouter(trailing_slash=False)
router.register("restaurants/menus", MenuApi, "restaurant-menu")
router.register("restaurants/menus/item", MenuItemApi, "restaurant-menu")

urlpatterns = router.urls

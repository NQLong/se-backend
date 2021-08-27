from oauth.views.bearer_authenticate import BearerAuthenticateApi
from django.urls import path, include
from rest_framework import routers


router = routers.DefaultRouter(trailing_slash=False)
router.register(prefix='auth', viewset=BearerAuthenticateApi, basename='donor')

urlpatterns = router.urls

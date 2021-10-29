from rest_framework import routers, urlpatterns
from .views import MediaAPI

router = routers.DefaultRouter(trailing_slash=False)
router.register('medias', MediaAPI, basename='medias')

urlpatterns = router.urls

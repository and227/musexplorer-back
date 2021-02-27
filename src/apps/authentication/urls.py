from rest_framework import routers
from rest_framework.authtoken import views

from .views import AuthViewSet

router = routers.SimpleRouter(trailing_slash=False)
router.register('', AuthViewSet, basename='auth')

urlpatterns = router.urls
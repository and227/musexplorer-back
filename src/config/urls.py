from django.contrib import admin
from django.urls import path, include
from src.apps.muzservice.urls import router
from src.config.settings import STATIC_URL, STATIC_ROOT
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('auth/', include("src.apps.auth.urls")),
    path('o/', include('oauth2_provider.urls', namespace='oauth2_provider')),
] 

from django.contrib import admin
from django.urls import path, include, re_path
from src.apps.muzservice.urls import router
from src.config.settings import STATIC_URL, STATIC_ROOT
from django.conf.urls.static import static
from django.conf.urls import url
from django.views.generic import RedirectView
from django.views.generic import TemplateView
import os
from .settings import BASE_DIR 

urlpatterns = [
    path("", TemplateView.as_view(template_name='index.html'), name='app'),
    path('oauth_test/', TemplateView.as_view(template_name='oauth_test.html')),
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('auth/', include("src.apps.authentication.urls")),
    path('accounts/', include('allauth.urls')),
]


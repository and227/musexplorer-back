from django.urls import path
from rest_framework.routers import Route, DynamicRoute, SimpleRouter
from .views import GroupViewSet, AlbumViewSet, TrackViewSet # , ArtistViewSet, TagViewSet, GenreViewSet

urlpatterns = []

router = SimpleRouter()
router.register(r'albums', AlbumViewSet, basename='album')
router.register(r'tracks', TrackViewSet, basename='track')
router.register(r'groups', GroupViewSet, basename='group')
# router.register(r'artists', ArtistViewSet, basename='artist')
# router.register(r'tags', TagViewSet, basename='tag')
# router.register(r'genres', GenreViewSet, basename='genre')
urlpatterns += router.urls
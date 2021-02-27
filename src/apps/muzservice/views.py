from django.shortcuts import render

import json
import os
import uuid

from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework.decorators import action
from django.shortcuts import get_object_or_404
from rest_framework.authentication import SessionAuthentication, \
    TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.serializers import ValidationError

# from src.config.settings import MEDIA_ROOT

from .pagination import ListDataPagination, get_pagination_queryset
from .models import Track, Album
from .serializers import AlbumSerializer, TrackSerializer
# from .services.image import upload_new_photo

from .mixins import ViewObjectMixin
from .renderers import ViewObjectRenderer
from .services import get_albums, get_tracks

class MuzserviceViewSet(viewsets.GenericViewSet, ViewObjectMixin):
    lookup_field = 'uuid'
    pagination_class = ListDataPagination
    # authentication_classes = [TokenAuthentication]
    # permission_classes = [IsAuthenticated]
    renderer_classes = [ViewObjectRenderer]


class AlbumViewSet(MuzserviceViewSet):
    serializer_class = AlbumSerializer

    def list(self, request):
        """ 
        Отдаем список альбомов в зависимости от параметров запроса
        """

        uuids = self.request.query_params.get('uuids', None)
        genre_uuids = self.request.query_params.get('genre', None)
        if uuids:
            uuids = uuids.replace('{', '').replace('}', '').split(',')
        if genre_uuids:
            genre_uuids = genre_uuids.replace('{', '').replace('}', '').split(',')
        queryset = get_albums(album_uuids=uuids, genre_uuids=genre_uuids)
        data = self.get_response_data(queryset)
        return Response(data)

    def retrieve(self, request, uuid=None):
        queryset = self.get_queryset()
        album = get_object_or_404(queryset, uuid=uuid)
        data = self.get_response_data(album)
        return Response(data)

    def create(self, request):
        try:
            data: dict = json.loads(request.body)
            categories: List[str] = data.pop('categories')
            serializer = AlbumSerializer(data=data)
            if serializer.is_valid(raise_exception=True):
                album: Album = serializer.save()
                album.categories.add(*categories)
                album.save()
            data = serializer.validated_data
        except ValidationError as error:
            data = error
        return Response(data)

    def update(self, request, uuid=None):
        try:
            queryset = self.get_queryset()
            album: Album = get_object_or_404(queryset, uuid=uuid)
            data: dict = json.loads(request.body)
            categories: List[str] = data.pop('categories')
            album.categories.add(*categories)
            album.save()
            serializer = AlbumSerializer(
                instance=album,
                data=data)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
            data = serializer.data
        except ValidationError as error:
            data = error
        return Response(data)

    def destroy(self, request, uuid=None):
        queryset = self.get_queryset()
        album = get_object_or_404(queryset, uuid=uuid)
        album.delete()
        return Response(None)

class TrackViewSet(MuzserviceViewSet):
    serializer_class = TrackSerializer

    def list(self, request):
        tracks_uuids = self.request.query_params.get('uuids', None)
        albums_uuids = self.request.query_params.get('albums', None)
        if tracks_uuids:
            tracks_uuids = tracks_uuids.replace('{', '').replace('}', '').split(',')
        if albums_uuids:
            albums_uuids = albums_uuids.replace('{', '').replace('}', '').split(',')
        queryset = get_tracks(tracks_uuids=tracks_uuids, albums_uuids=albums_uuids) 
        data = self.get_response_data(queryset)
        return Response(data)

    def retrieve(self, request, uuid=None):
        queryset = self.get_queryset()
        photo = get_object_or_404(queryset, uuid=uuid)
        data = self.get_response_data(photo)
        return Response(data)

    def destroy(self, request, uuid=None):
        print("destroy")
        queryset = self.get_queryset()
        photo = get_object_or_404(queryset, uuid=uuid)
        photo.delete()
        return Response(None)

    def create(self, request):
        return Response(None)


# class GenreViewSet(MuzserviceViewSet):
#     serializer_class = CategoryWithPhotoSerializer
#     queryset = Category.objects.all()

#     def list(self, request):
#         queryset = self.get_queryset()
#         data = self.get_response_data(queryset)
#         return Response(data)

#     def retrieve(self, request, uuid=None):
#         queryset = self.get_queryset()
#         category = get_object_or_404(queryset, uuid=uuid)
#         data = self.get_response_data(category)
#         return Response(data)

#     def create(self, request):
#         try:
#             serializer = CategorySerializer(
#                 data=json.loads(request.body))
#             if serializer.is_valid(raise_exception=True):
#                 category = serializer.save()
#             data = serializer.data 
#         except ValidationError as error:
#             data = error
#         return Response(data)

#     def update(self, request, uuid=None):
#         try:
#             queryset = self.get_queryset()
#             category = get_object_or_404(queryset, uuid=uuid)
#             serializer = CategorySerializer(
#                 instance=category,
#                 data=json.loads(request.body))
#             if serializer.is_valid(raise_exception=True):
#                 serializer.save()
#             data = serializer.data
#         except ValidationError as error:
#             data = error
#         return Response(data)

#     def destroy(self, request, uuid=None):
#         queryset = self.get_queryset()
#         album = get_object_or_404(queryset, uuid=uuid)
#         album.delete()
#         return Response(None)




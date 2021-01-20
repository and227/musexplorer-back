import os
from rest_framework import serializers
# from src.config.settings import MEDIA_URL

from .models import Track, Album, Group

class TrackSerializer(serializers.ModelSerializer):
    # images = IMGSerializer(read_only=True, many=True)

    class Meta:
        model = Track
        fields = '__all__' # ('track_uuid', 'name', 'images', 'created_at', 'updated_at', 'is_active')


class AlbumSerializer(serializers.ModelSerializer):
    # photos = PhotoSerializer(read_only=True, many=True, required=False)
    # categories = CategorySerializer(read_only=True, many=True, required=False)

    class Meta:
        model = Album
        fields = '__all__'
        extra_kwargs = {
            'is_active': {'required': False},
            'created_at': {'required': False},
            'updated_at': {'required': False},
            'uuid': {'required': False}
        }

class GroupSerializer(serializers.ModelSerializer):

    class Meta:
        model = Group
        fields = '__all__'
        
        extra_kwargs = {
            'is_active': {'required': False},
            'created_at': {'required': False},
            'updated_at': {'required': False},
            'uuid': {'required': False}
        }
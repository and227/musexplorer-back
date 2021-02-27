from rest_framework import renderers
from .pagination import get_pagination_queryset, is_one_page
from .response_struct import StatusResponse, ViewObject
from django.shortcuts import get_object_or_404
from django.http import Http404


class ViewObjectRenderer(renderers.BaseRenderer):
    media_type = 'application/json'
    format = 'json'

    def render(self, data, media_type=None, renderer_context=None):   
        if 'detail' in data:
            response = ViewObject(
                status='fail', data=data['detail'])    
        else:
            response = ViewObject(
                status='success', data=data)
 
        return response.to_json()
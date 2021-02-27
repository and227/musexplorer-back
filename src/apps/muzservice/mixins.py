from rest_framework import renderers
from .pagination import get_pagination_queryset, is_one_page
from django.shortcuts import get_object_or_404



class ViewObjectMixin:
    def get_response_data(self, query_objects):
        # подготавливаем список если метод list
        if self.action == 'list':
            # если количество объектов не помещается на одну страницу
            if not is_one_page(query_objects):
                page = self.paginate_queryset(query_objects)            
                page_num = int(self.request.query_params.get('page', 1))
                serializer = self.serializer_class(
                    instance=get_pagination_queryset(
                        page_num, 
                        query_objects), 
                    many=True)
                paginated = self.get_paginated_response(
                    serializer.data)
                data = paginated.data
            else:
                serializer = self.serializer_class(
                    instance=query_objects, many=True)
                data = serializer.data
        else:
            serializer = self.serializer_class(
                instance=query_objects)
            data = serializer.data
 
        return data
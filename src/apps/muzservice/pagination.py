from rest_framework import pagination
from rest_framework.response import Response
from rest_framework.utils.urls import replace_query_param, remove_query_param

from src.config.settings import DEFAULT_PAGE, DEFAULT_PAGE_SIZE, DEFAULT_OBJECT_PAGE_SIZE

def is_one_page(queryset):
    if queryset.model.__name__ in DEFAULT_OBJECT_PAGE_SIZE:
        page_size = DEFAULT_OBJECT_PAGE_SIZE[queryset.model.__name__]
    else:
        page_size = DEFAULT_PAGE_SIZE 

    if len(queryset) <= page_size:
        return True

    return False


def get_pagination_queryset(page_num, queryset):
    if queryset.model.__name__ in DEFAULT_OBJECT_PAGE_SIZE:
        page_size = DEFAULT_OBJECT_PAGE_SIZE[queryset.model.__name__]
        start = (page_num - 1) * page_size
        end = page_num * page_size
    else:
        start = (page_num - 1) * DEFAULT_PAGE_SIZE
        end = page_num * DEFAULT_PAGE_SIZE

    return queryset[start:end]

class ListDataPagination(pagination.PageNumberPagination):
    page = DEFAULT_PAGE
    page_size = DEFAULT_PAGE_SIZE
    page_size_query_param = 'page_size'

    def paginate_queryset(self, queryset, request, view=None):
        if queryset.model.__name__ in DEFAULT_OBJECT_PAGE_SIZE:
            self.page_size = DEFAULT_OBJECT_PAGE_SIZE[queryset.model.__name__]
        return super().paginate_queryset(queryset, request, view)

    def get_first_link(self):
        url = self.request.build_absolute_uri()       
        if not self.page.has_previous():
            return None
        page_number = self.page.paginator.validate_number(1)
        return replace_query_param(url, self.page_query_param, page_number)

    def get_last_link(self):
        url = self.request.build_absolute_uri()
        if not self.page.has_next():
            return None
        page_number = self.page.paginator.validate_number(
            self.page.paginator.num_pages)

        return replace_query_param(url, self.page_query_param, page_number)

    def get_paginated_response(self, data):
        return Response({
                'total': self.page.paginator.count,
                'count': len(data),
                'current_page': self.page.number,
                'links': {
                    "first": self.get_first_link(),
                    "prev": self.get_previous_link(),
                    "next": self.get_next_link(),
                    "last": self.get_last_link()              
                },
                'data': data 
            })        



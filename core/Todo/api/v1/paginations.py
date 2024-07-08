from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter

class DefaultPagination(PageNumberPagination):
    page_size = 10

    def get_paginated_response(self, data):
<<<<<<< HEAD
        filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
        filterset_fields = {'author': ["exact"],
                        'title': ["exact"], 'status': ["exact"]}
        search_fields = ['title', 'content']
        ordering_fields = ['created_date', ]
=======
>>>>>>> authentications-api
        return Response(
            {
                "links": {
                    "next": self.get_next_link(),
                    "previous": self.get_previous_link(),
                },
<<<<<<< HEAD
                "total_objects": self.page.paginator.count,
                "total_pages": self.page.paginator.num_pages,
                "results": data,
                "filterset_fields": filterset_fields,
                "search_fields": search_fields,
                "ordering_fields": ordering_fields,
            }
        )
    
=======
                "total_object": self.page.paginator.count,
                "total_pages": self.page.paginator.num_pages,
                "result": data,
            }
        )
>>>>>>> authentications-api

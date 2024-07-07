from rest_framework.pagination import *


class pagination(PageNumberPagination):
    page_size = 2

    def get_paginated_response(self, data):
        return Response(
            {
                "links": {
                    "next": self.get_next_link(),
                    "previous": self.get_previous_link(),
                },
                "total_object": self.page.paginator.count,
                "total_pages": self.page.paginator.num_pages,
                "result": data,
            }
        )

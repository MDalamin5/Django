from rest_framework.pagination import PageNumberPagination, LimitOffsetPagination, CursorPagination

class ProductPagination(PageNumberPagination):
    page_size = 3 # total 10 product 3 3 3 1
    page_query_param = 'p'
    page_size_query_param = 'size'
    max_page_size = 4


class ProductLimitOffsetPagination(LimitOffsetPagination):
    default_limit = 3
    limit_query_param = 'l'
    offset_query_param = 'start'

class ProductCursorPagination(CursorPagination):
    page_size = 3
    ordering = 'price'
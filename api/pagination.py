from rest_framework.pagination import PageNumberPagination, LimitOffsetPagination, CursorPagination


class CandidatePagination(PageNumberPagination):
    page_size = 3
    page_query_param = 'p'
    page_size_query_param = 'size'
    max_page_size = 10

# class CandidatePaginationLO(LimitOffsetPagination):
#     default_limit = 5
#     max_limit = 10
#     limit_query_param = 'limit'
#     offset_query_param = 'start'
# this is for limit offset , limit mean - page size
# and offset mean - from where we want next 5(size elements)

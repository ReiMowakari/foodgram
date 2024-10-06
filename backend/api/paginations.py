from rest_framework.pagination import PageNumberPagination

# Константа для кол-ва отображения страниц.
PAGE_NUMBER = 2


class LimitPageNumberPagination(PageNumberPagination):
    """Класс для пагинации."""

    page_size = 2
    page_size_query_param = 'limit'

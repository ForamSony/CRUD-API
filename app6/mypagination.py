from rest_framework.pagination import PageNumberPagination,LimitOffsetPagination

# class My(PageNumberPagination):
#     page_size = 5 # 5 record in 1 page
#     page_query_param = 'p'
#     page_size_query_param = 'recordes' #userchoice howmuch records in singlepage
#     max_page_size = 6 # maxi records in singlepage
#     last_page_strings = 'end'

class Mylimit(LimitOffsetPagination):
   default_limit = 5
   # limit_query_param = 'l'
   # offset_query_param = 'o'
   max_limit = 6
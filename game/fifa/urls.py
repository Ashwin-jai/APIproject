from .views import *
from django.urls import  path
urlpatterns=[
    path('main/',create_employee),
    path('get/',getrecords),
    path('all/',get_allrecord),
    path('filter/',filter_record),
    path('update/',update_record),
    path('delete/',delete_record),

    ]
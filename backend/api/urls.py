from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from api.views import (
    HostAPI,
    HostDetailAPI,
    SQLAPI,
    SQLDetailAPI,
    DataAPI,
    DataDetailAPI,
)

urlpatterns = [
    path('host/', HostAPI.as_view(), name='host'),
    path('host/<int:pk>/', HostDetailAPI.as_view(), name='host_detail'),
    path('sql/', SQLAPI.as_view(), name='sql'),
    path('sql/<int:pk>/', SQLDetailAPI.as_view(), name='sql_detail'),
    path('data/', DataAPI.as_view(), name='data'),
    path('data/<int:pk>/', DataDetailAPI.as_view(), name='data_detail'),
]

urlpatterns = format_suffix_patterns(urlpatterns)
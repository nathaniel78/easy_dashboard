from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from api.views import (
    HostAPI,
    HostDetailAPI,
    SQLAPI,
    SQLDetailAPI,
    DataAPI,
    DataDetailAPI,
    DashboardAPI,
    DashboardDetailAPI,
    ChartAPI,
    ChartDetailAPI,
)

urlpatterns = [
    path('host/', HostAPI.as_view(), name='host'),
    path('host/<int:pk>/', HostDetailAPI.as_view(), name='host_detail'),
    path('sql/', SQLAPI.as_view(), name='sql'),
    path('sql/<int:pk>/', SQLDetailAPI.as_view(), name='sql_detail'),
    path('data/', DataAPI.as_view(), name='data'),
    path('data/<int:pk>/', DataDetailAPI.as_view(), name='data_detail'),
    path('dashboard/', DashboardAPI.as_view(), name='dashboard'),
    path('dashboard/<int:pk>/', DashboardDetailAPI.as_view(), name='dashboard_detail'),
    path('chart/', ChartAPI.as_view(), name='chart'),
    path('chart/<int:pk>/', ChartDetailAPI.as_view(), name='chart_detail'),
]

urlpatterns = format_suffix_patterns(urlpatterns)
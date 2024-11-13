from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from .models import (
    Host,
    SQL,
    Data,
    Dashboard,
    Chart
)
from .serializers import (
    HostSerializar,
    SQLSerializer,
    DataSerializer,
    DashboardSerializer,
    ChartSerializer
)


# View Host
class HostViewAPI(viewsets.ModelViewSet):
    def get(self, request):
        hosts = Host.objects.all()
        serializer = HostSerializar(hosts, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
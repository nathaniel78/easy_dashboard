from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.views import APIView
from .models import (
    Host,
    SQL,
    Data,
)
from .serializers import (
    HostSerializar,
    SQLSerializer,
    DataSerializer,
)


# View Host
class HostAPI(APIView):
    # List
    def get(self, request):
        hosts = Host.objects.all()
        serializer = HostSerializar(hosts, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    # Create
    def post(self, request):
        serialiazer = HostSerializar(data=request.data)
        if serialiazer.is_valid():
            serialiazer.save()
            return Response(serialiazer.data, status=status.HTTP_201_CREATED)
        return Response(serialiazer.errors, status=status.HTTP_400_BAD_REQUEST)
    

# View HostDetail
class HostDetailAPI(APIView):
    # Validate
    def get_object(self, pk):
        return get_object_or_404(Host, pk=pk)
    
    # Detail
    def get(self, request, pk):
        host = self.get_object(pk)
        serializer = HostSerializar(host)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    # Update
    def put(self, request, pk):
        host = self.get_object(pk)
        serializer = HostSerializar(host, data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    # Delete
    def delete(self, request, pk):
        host = self.get_object(pk)
        host.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    

# View SQL
class SQLAPI(APIView):
    # List
    def get(self, request):
        sql = SQL.objects.all()
        serializer = SQLSerializer(sql, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    # Create
    def post(self, request):
        serializer = SQLSerializer(data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
# View SQLDetail
class SQLDetailAPI(APIView):
    # Validate
    def get_object(self, pk):
        return get_object_or_404(SQL, pk=pk)
    
    # Detail
    def get(self, request, pk):
        sql = self.get_object(pk)
        serializer = SQLSerializer(sql)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    # Update
    def put(self, request, pk):
        sql = self.get_object(pk)
        serializer = SQLSerializer(sql, data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    # Delete
    def delete(self, request, pk):
        sql = self.get_object(pk)
        sql.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    

# View Data
class DataAPI(APIView):
    # List
    def get(self, request):
        data = Data.objects.all()
        serializer = DataSerializer(data, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    # Create
    def post(self, request):
        serializer = DataSerializer(data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
# View DataDetail
class DataDetailAPI(APIView):
    # Validate
    def get_object(self, pk):
        return get_object_or_404(Data, pk=pk)
    
    # Detail
    def get(self, request, pk):
        data = self.get_object(pk)
        serializer = DataSerializer(data)        
        return Response(serializer.data, status=status.HTTP_200_OK)
        
    # Update
    def put(self, request, pk):
        data = self.get_object(pk)
        serializer = DataSerializer(data, data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    # Delete
    def delete(self, request, pk):
        data = self.get_object(pk)
        data.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

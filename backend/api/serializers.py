from rest_framework import serializers
from api.models import (
    Host, 
    SQL, 
    Data, 
)


# Serializer Host
class HostSerializar(serializers.ModelSerializer):
    class Meta:
        model = Host
        fields = '__all__'
        

# Serializer SQL
class SQLSerializer(serializers.ModelSerializer):
    class Meta:
        model =SQL
        fields = '__all__'
        

# Serializer Data
class DataSerializer(serializers.ModelSerializer):
    class Meta:
        model =Data
        fields = '__all__'

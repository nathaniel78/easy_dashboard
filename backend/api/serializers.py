from rest_framework import serializers
from models import Host, SQL, Data, Dashboard, Chart


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
        

# Serializer Dashboard
class DashboardSerializer(serializers.ModelSerializer):
    class Meta:
        model =Dashboard
        fields = '__all__'
        
        
# Serializer Chart
class ChartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chart
        fields = '__all__'
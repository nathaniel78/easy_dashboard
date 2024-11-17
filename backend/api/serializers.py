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
        
    # Validação    
    def validate(self, data):
        type_chart = data.get('type_chart')
        if type_chart not in [1, 2, 3]:
            raise serializers.ValidationError("Valores aceitos: 1 (barra empilhada), 2 (area empilhada), 3 (bolha empilhada)")

        return data

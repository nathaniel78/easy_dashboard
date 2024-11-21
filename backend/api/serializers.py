from rest_framework import serializers
import json
from api.models import (
    Host, 
    SQL, 
    Data, 
)

# TODO: Serializer Host
class HostSerializar(serializers.ModelSerializer):
    class Meta:
        model = Host
        fields = '__all__'
        

# TODO: Serializer SQL
class SQLSerializer(serializers.ModelSerializer):
    class Meta:
        model =SQL
        fields = '__all__'
        

# TODO: Serializer Data
class DataSerializer(serializers.ModelSerializer):
    class Meta:
        model =Data
        fields = '__all__'
        
     # TODO: Function to_representation
    def to_representation(self, instance):
        representation = super().to_representation(instance)
        
        # Verifica se o campo 'data_json' existe e converte
        if 'data_json' in representation:
            try:
                representation['data_json'] = json.loads(representation['data_json'])
            except (json.JSONDecodeError, TypeError):
                representation['data_json'] = {}

        return representation

    # TODO: Function to_internal_value
    def to_internal_value(self, data):
        # Converte 'data_json' de volta para o formato de string JSON, se for um objeto
        if 'data_json' in data:
            try:
                data['data_json'] = json.dumps(data['data_json'])
            except (TypeError, ValueError):
                raise serializers.ValidationError({"data_json": "Invalid data format. Expected a JSON-serializable object."})

        return super().to_internal_value(data)
        
    # TODO: Validation    
    def validate(self, data):
        type_chart = data.get('type_chart')
        if type_chart not in [1, 2, 3, 4]:
            raise serializers.ValidationError("Valores aceitos: 1 (barra empilhada), 2 (area empilhada), 3 (bolha empilhada), 4 (barra horizontal)")

        return data

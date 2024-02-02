# En serializers.py
from rest_framework import serializers
from .models import Infraccion, Policia


class InfraccionPayloadSerializer(serializers.Serializer):
    placa_patente = serializers.CharField(max_length=20)
    timestamp = serializers.DateTimeField()
    comentarios = serializers.CharField()
    numero_identificativo_oficial = serializers.IntegerField()

    def validate_numero_identificativo_oficial(self, value):
        try:
            Policia.objects.get(id=value)
            return value
        except Policia.DoesNotExist:
            raise serializers.ValidationError("Oficial no encontrado.")


class InfraccionSerializer(serializers.ModelSerializer):

    nombre_oficial = serializers.\
        ReadOnlyField(source='policia.user.get_full_name')

    class Meta:
        model = Infraccion
        fields = '__all__'

from rest_framework import serializers
from .models import GestionCorreo, Encuestas, Incidentes, Solicitudes

class GestionCorreoSerializer(serializers.ModelSerializer):
    class Meta:
        model = GestionCorreo
        fields = '__all__'

class EncuestasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Encuestas
        fields = '__all__'

class IncidentesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Incidentes
        fields = '__all__'

class SolicitudesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Solicitudes
        fields = '__all__'


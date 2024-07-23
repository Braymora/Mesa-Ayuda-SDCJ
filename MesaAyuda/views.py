from django.shortcuts import render
from rest_framework import viewsets
from .models import GestionCorreo, Encuestas, Incidentes, Solicitudes
from .serializers import GestionCorreoSerializer, EncuestasSerializer, IncidentesSerializer, SolicitudesSerializer

class GestionCorreoViewSet(viewsets.ModelViewSet):
    queryset = GestionCorreo.objects.all()
    serializer_class = GestionCorreoSerializer

class EncuestasViewSet(viewsets.ModelViewSet):
    queryset = Encuestas.objects.all()
    serializer_class = EncuestasSerializer

class IncidentesViewSet(viewsets.ModelViewSet):
    queryset = Incidentes.objects.all()
    serializer_class = IncidentesSerializer

class SolicitudesViewSet(viewsets.ModelViewSet):
    queryset = Solicitudes.objects.all()
    serializer_class = SolicitudesSerializer


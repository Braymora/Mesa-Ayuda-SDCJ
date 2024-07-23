from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from MesaAyuda.views import GestionCorreoViewSet, EncuestasViewSet, IncidentesViewSet, SolicitudesViewSet

router = DefaultRouter()
router.register(r'gestioncorreo', GestionCorreoViewSet)
router.register(r'encuestas', EncuestasViewSet)
router.register(r'incidentes', IncidentesViewSet)
router.register(r'solicitudes', SolicitudesViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),  # Incluye la URL del admin
    path('', include(router.urls)),
]

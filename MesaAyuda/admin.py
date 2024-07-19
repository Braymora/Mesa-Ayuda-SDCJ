from django.contrib import admin
from .models import GestionCorreo, Encuestas, Incidentes, Solicitudes

# Registra los modelos en el admin
admin.site.register(GestionCorreo)
admin.site.register(Encuestas)
admin.site.register(Incidentes)
admin.site.register(Solicitudes)
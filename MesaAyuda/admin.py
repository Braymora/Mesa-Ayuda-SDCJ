from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin
from .models import GestionCorreo, Encuestas, Incidentes, Solicitudes
from .resources import GestionCorreoResource, EncuestasResource, IncidentesResource, SolicitudesResource

class GestionCorreoResource(resources.ModelResource):
    class Meta:
        model = GestionCorreo
        fields = (
            'Fecha', 'Total', 'ConTicket', 'SinTicket', 'SandyConTicket', 
            'SandySinTicket', 'LizethConTicket', 'LizethSinTicket', 'ElkinConTicket', 
            'ElkinSinTicket', 'JaimeConTicket', 'JaimeSinTicket', 'MaycolConTicket', 
            'MaycolSinTicket', 'JefersonConTicket', 'JefersonSinTicket', 'JorgeConTicket', 
            'JorgeSinTicket', 'AndersonConTicket', 'AndersonSinTicket', 'YairConTicket', 
            'YairSinTicket', 'XavierConTicket', 'XavierSinTicket', 'YessicaConTicket', 
            'YessicaSinTicket', 'JeffersonConTicket', 'JeffersonSinTicket', 'DianaConTicket', 
            'DianaSinTicket', 'GerardoConTicket', 'GerardoSinTicket', 'AndresConTicket', 
            'AndresSinTicket', 'JhonatanConTicket', 'JhonatanSinTicket', 'YenyConTicket', 
            'YenySinTicket'
        )
        
# Registra los modelos en el admin
@admin.register(GestionCorreo)
class GestionCorreoAdmin(ImportExportModelAdmin):
    resource_class = GestionCorreoResource


class EncuestasResource(resources.ModelResource):
    class Meta:
        model = Encuestas
        fields = (
            'CreadoPor', 
            'FechaRespuestaEncuesta', 
            'Ticket', 
            'Agente', 
            'MedioDeAccesoMesaDeServicio', 
            'NivelDeSatisfacciónSolucionSolicitud', 
            'NivelDeSatisfacciónTiempoSolucion', 
            'CalificacionDelAgente', 
            'Encuesta', 
            'Comentarios', 
            'Calificacion0a5', 
            'TipoDeElemento', 
            'RutaDeAcceso'
        )

@admin.register(Encuestas)
class EncuestasAdmin(ImportExportModelAdmin):
    resource_class = EncuestasResource


class IncidentesResource(resources.ModelResource):
    class Meta:
        model = Incidentes
        fields = (
            'IdIncidentes', 'AssignedUser', 'Title', 'Status', 'Services', 
            'CreatedDate', 'ResolvedDate', 'ClosedDate', 'AffectedUser', 'GrupoSoporte', 
            'Source'
        )

@admin.register(Incidentes)
class IncidentesAdmin(ImportExportModelAdmin):
    resource_class = IncidentesResource
 

class SolicitudesResource(resources.ModelResource):
    class Meta:
        model = Solicitudes
        fields = (
            'IdSolicitud', 'AssignedUser1', 'Title1', 'Status1', 'Services1', 
            'Services2', 'CreatedDate1', 'ResolvedDate1', 'ClosedDate', 'AffectedUser1', 
            'GrupoSoporte1', 'Origen', 'Description'
        )    

@admin.register(Solicitudes)
class SolicitudesAdmin(ImportExportModelAdmin):
    resource_class = SolicitudesResource


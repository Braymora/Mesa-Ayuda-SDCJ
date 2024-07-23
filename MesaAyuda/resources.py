from import_export import resources
from import_export.fields import Field
from .models import GestionCorreo, Encuestas, Incidentes, Solicitudes

class GestionCorreoResource(resources.ModelResource):
    class Meta:
        model = GestionCorreo

class EncuestasResource(resources.ModelResource):
    # Campos definidos explícitamente
    CreadoPor = Field(attribute='CreadoPor', column_name='CreadoPor')
    FechaRespuestaEncuesta = Field(attribute='FechaRespuestaEncuesta', column_name='FechaRespuestaEncuesta')
    Ticket = Field(attribute='Ticket', column_name='Ticket')
    Agente = Field(attribute='Agente', column_name='Agente')
    MedioDeAccesoMesaDeServicio = Field(attribute='MedioDeAccesoMesaDeServicio', column_name='MedioDeAccesoMesaDeServicio')
    NivelDeSatisfaccionSolucionSolicitud = Field(attribute='NivelDeSatisfaccionSolucionSolicitud', column_name='NivelDeSatisfaccionSolucionSolicitud')
    NivelDeSatisfaccionTiempoSolucion = Field(attribute='NivelDeSatisfaccionTiempoSolucion', column_name='NivelDeSatisfaccionTiempoSolucion')
    CalificacionDelAgente = Field(attribute='CalificacionDelAgente', column_name='CalificacionDelAgente')
    Encuesta = Field(attribute='Encuesta', column_name='Encuesta')
    Comentarios = Field(attribute='Comentarios', column_name='Comentarios')
    Calificacion0a5 = Field(attribute='Calificacion0a5', column_name='Calificacion0a5')
    TipoDeElemento = Field(attribute='TipoDeElemento', column_name='TipoDeElemento')
    RutaDeAcceso = Field(attribute='RutaDeAcceso', column_name='RutaDeAcceso')

    def before_import_row(self, row, **kwargs):
        print(row)  # Esto imprimirá cada fila del archivo en la consola

    class Meta:
        model = Encuestas
        fields = (
            'CreadoPor', 'FechaRespuestaEncuesta', 'Ticket', 'Agente', 
            'MedioDeAccesoMesaDeServicio', 'NivelDeSatisfacciónSolucionSolicitud', 
            'NivelDeSatisfacciónTiempoSolucion', 'CalificacionDelAgente', 'Encuesta', 
            'Comentarios', 'Calificacion0a5', 'TipoDeElemento', 'RutaDeAcceso'
        )

class IncidentesResource(resources.ModelResource):
    class Meta:
        model = Incidentes

class SolicitudesResource(resources.ModelResource):
    class Meta:
        model = Solicitudes

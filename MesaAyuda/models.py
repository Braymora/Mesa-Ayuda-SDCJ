from django.db import models

# Create your models here.

class GestionCorreo(models.Model):
    
    # Data de Correo may2024
    # GESTION DE CORREO

    Fecha = models.DateField(verbose_name="FECHA")
    Total = models.CharField(max_length=255, verbose_name="TOTAL")
    ConTicket = models.CharField(max_length=255, verbose_name="ConTicket")
    SinTicket = models.CharField(max_length=255, verbose_name="SinTicket")

    SandyConTicket = models.CharField(max_length=255, verbose_name="SandyConTicket")
    SandySinTicket = models.CharField(max_length=255, verbose_name="SandySinTicket")

    LizethConTicket = models.CharField(max_length=255, verbose_name="LizethConTicket")
    LizethSinTicket = models.CharField(max_length=255, verbose_name="LizethSinTicket")

    ElkinConTicket = models.CharField(max_length=255, verbose_name="ElkinConTicket")
    ElkinSinTicket = models.CharField(max_length=255, verbose_name="ElkinSinTicket")

    JaimeConTicket = models.CharField(max_length=255, verbose_name="JaimeConTicket")
    JaimeSinTicket = models.CharField(max_length=255, verbose_name="JaimeSinTicket")

    MaycolConTicket = models.CharField(max_length=255, verbose_name="MaycolConTicket")
    MaycolSinTicket = models.CharField(max_length=255, verbose_name="MaycolSinTicket")

    JefersonConTicket = models.CharField(max_length=255, verbose_name="JefersonConTicket")
    JefersonSinTicket = models.CharField(max_length=255, verbose_name="JefersonSinTicket")

    JorgeConTicket = models.CharField(max_length=255, verbose_name="JorgeConTicket")
    JorgeSinTicket = models.CharField(max_length=255, verbose_name="JorgeSinTicket")

    AndersonConTicket = models.CharField(max_length=255, verbose_name="AndersonConTicket")
    AndersonSinTicket = models.CharField(max_length=255, verbose_name="AndersonSinTicket")

    YairConTicket = models.CharField(max_length=255, verbose_name="YairConTicket")
    YairSinTicket = models.CharField(max_length=255, verbose_name="YairSinTicket")

    XavierConTicket = models.CharField(max_length=255, verbose_name="XavierConTicket")
    XavierSinTicket = models.CharField(max_length=255, verbose_name="XavierSinTicket")

    YessicaConTicket = models.CharField(max_length=255, verbose_name="YessicaConTicket")
    YessicaSinTicket = models.CharField(max_length=255, verbose_name="YessicaSinTicket")

    JeffersonConTicket = models.CharField(max_length=255, verbose_name="JeffersonConTicket")
    JeffersonSinTicket = models.CharField(max_length=255, verbose_name="JeffersonSinTicket")

    DianaConTicket = models.CharField(max_length=255, verbose_name="DianaConTicket")
    DianaSinTicket = models.CharField(max_length=255, verbose_name="DianaSinTicket")

    GerardoConTicket = models.CharField(max_length=255, verbose_name="GerardoConTicket")
    GerardoSinTicket = models.CharField(max_length=255, verbose_name="GerardoSinTicket")

    AndresConTicket = models.CharField(max_length=255, verbose_name="AndresConTicket")
    AndresSinTicket = models.CharField(max_length=255, verbose_name="AndresSinTicket")

    JhonatanConTicket = models.CharField(max_length=255, verbose_name="JhonatanConTicket")
    JhonatanSinTicket = models.CharField(max_length=255, verbose_name="JhonatanSinTicket")

    YenyConTicket = models.CharField(max_length=255, verbose_name="YenyConTicket")
    YenySinTicket = models.CharField(max_length=255, verbose_name="YenySinTicket")


class Encuestas(models.Model):
    # Data encuestas mayo2024
    # query
    CreadoPor = models.CharField(max_length=255, verbose_name="CreadoPor")
    FechaRespuestaEncuesta = models.DateTimeField(verbose_name="FechaRespuestaEncuesta")
    Ticket = models.CharField(max_length=255)
    Agente = models.CharField(max_length=255, verbose_name="Agente")
    MedioDeAccesoMesaDeServicio = models.CharField(max_length=255)
    NivelDeSatisfaccionSolucionSolicitud = models.CharField(max_length=255)
    NivelDeSatisfaccionTiempoSolucion = models.CharField(max_length=255)
    CalificacionDelAgente = models.CharField(max_length=255)
    Encuesta = models.CharField(max_length=255)
    Comentarios = models.CharField(max_length=255)
    Calificacion0a5 = models.CharField(max_length=255)
    TipoDeElemento = models.CharField(max_length=255)
    RutaDeAcceso = models.CharField(max_length=255)


class Incidentes(models.Model):
    # Incidentes mayo 2024
    # Sheet1
    IdIncidentes = models.CharField(max_length=255)
    AssignedUser = models.CharField(max_length=255, verbose_name="AssignedUser")
    Title = models.CharField(max_length=255, verbose_name="Title")
    Status = models.CharField(max_length=255, verbose_name="Status")
    Services = models.CharField(max_length=255, verbose_name="Services")
    CreatedDate = models.DateTimeField(verbose_name="CreatedDate")
    ResolvedDate = models.DateTimeField(verbose_name="ResolvedDate")
    ClosedDate = models.DateTimeField(verbose_name="ClosedDate")
    AffectedUser = models.CharField(max_length=255, verbose_name="AffectedUser")
    GrupoSoporte = models.CharField(max_length=255, verbose_name="GrupoSoporte")
    Source = models.CharField(max_length=255, verbose_name="Source")


class Solicitudes(models.Model):
    # Solicitudes mayo 2024
    IdSolicitud = models.CharField(max_length=255)
    AssignedUser1 = models.CharField(max_length=255, verbose_name="AssignedUser")
    Title1 = models.CharField(max_length=255, verbose_name="Title")
    Status1 = models.CharField(max_length=255, verbose_name="Status")
    Services1 = models.CharField(max_length=255, verbose_name="Services")
    Services2 = models.CharField(max_length=255, verbose_name="Services")
    CreatedDate1 = models.DateTimeField(verbose_name="CreatedDate")
    ResolvedDate1 = models.DateTimeField(verbose_name="ResolvedDate")
    ClosedDate = models.DateTimeField(verbose_name="ClosedDate")
    AffectedUser1 = models.CharField(max_length=255, verbose_name="AffectedUser")
    GrupoSoporte1 = models.CharField(max_length=255, verbose_name="GrupoSoporte")
    Origen = models.CharField(max_length=255, verbose_name="Origen")
    Description = models.CharField(max_length=255, verbose_name="Description")

from django.db import connection
from django.db.models import Count, F
from listaDeAsistenciaApp.models import *

def run():
    exposicion = F('ponderaciones__exposicion')
    participacion = F('ponderaciones__participacion')
    noticia = F('ponderaciones__noticia')
    alumnos = Alumno.objects.annotate(
        exposicion = exposicion, 
        participacion = participacion, 
        noticia = noticia
    )
    print(alumnos)
    # print(alumnos.values('asistencias'))
    print(connection.queries)




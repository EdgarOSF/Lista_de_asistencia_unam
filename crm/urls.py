from django.urls import path
from crm.views import AsistenciaAlumno, Index
from crm.views_alumno import *
from crm.views_clase import *

app_name = 'crm'

urlpatterns = [
    path('', Index.as_view(), name='index'),
    #Alumno
    path('alumno', IndexAlumno.as_view(), name='index_alumno'),
    path('alumno/detail/<int:pk>', AlumnoDetail.as_view(), name='alumno_detail'),
    path('alumno/create', AlumnoCreate.as_view(), name='alumno_create'),
    path('alumno/delete/<int:pk>', AlumnoDelete.as_view(), name='alumno_delete'),
    path('alumno/update/<int:pk>', AlumnoUpdate.as_view(), name='alumno_update'),
    #Clase
    path('clase', IndexClase.as_view(), name='index_clase'),
    path('clase/detail/<int:pk>', ClaseDetail.as_view(), name='clase_detail'),
    path('clase/create', ClaseCreate.as_view(), name='clase_create'),
    path('clase/delete/<int:pk>', ClaseDelete.as_view(), name='clase_delete'),
    path('clase/update/<int:pk>', ClaseUpdate.as_view(), name='clase_update'),
    # Asistencias
    path('asistencias/<int:id_alumno>', AsistenciaAlumno, name='asistencia_alumno')
]


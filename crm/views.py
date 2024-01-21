from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render
from django.views.generic import TemplateView, ListView

from listaDeAsistenciaApp.models import Alumno, Asistencia


class Index(TemplateView):
    template_name = "crm/index.html"


def AsistenciaAlumno(request, id_alumno):
    queryset = Asistencia.objects.filter(fk_alumno = id_alumno)

    return render(request, 'crm/asistencia_alumno.html', {'clases': queryset})
    

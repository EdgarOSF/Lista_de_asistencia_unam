from typing import Any
from django.db.models.query import QuerySet
from django.db.models import Count
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView

from crm.forms import AlumnoForm
from listaDeAsistenciaApp.models import Alumno


class IndexAlumno(ListView):
    model = Alumno
    template_name = 'crm/alumno/index.html'


class AlumnoCreate(CreateView):
    model = Alumno
    form_class = AlumnoForm
    template_name = 'crm/alumno/alumno_form.html'
    success_url = reverse_lazy('crm:index_alumno')


class AlumnoUpdate(UpdateView):
    model = Alumno
    form_class = AlumnoForm
    success_url = reverse_lazy('crm:index_alumno')
    template_name = 'crm/alumno/alumno_update_form.html'


class AlumnoDetail(DetailView):
    model = Alumno
    template_name = 'crm/alumno/alumno_detail.html'
    context_object_name = 'alumno'


class AlumnoDelete(DeleteView):
    model = Alumno
    template_name = 'crm/alumno/alumno_confirm_delete.html'
    success_url = reverse_lazy('crm:index_alumno')



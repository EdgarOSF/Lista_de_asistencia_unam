from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView

from crm.forms import ClaseForm
from listaDeAsistenciaApp.models import Clase


class IndexClase(ListView):
    model = Clase
    template_name = 'crm/clase/index.html'


class ClaseCreate(CreateView):
    model = Clase
    form_class = ClaseForm
    template_name = 'crm/clase/clase_form.html'
    success_url = reverse_lazy('crm:index_clase')


class ClaseUpdate(UpdateView):
    model = Clase
    form_class = ClaseForm
    template_name = 'crm/clase/clase_update_form.html'
    success_url = reverse_lazy('crm:index_clase')


class ClaseDetail(DetailView):
    model = Clase
    template_name = 'crm/clase/clase_detail.html'
    context_object_name = 'clase'


class ClaseDelete(DeleteView):
    model = Clase
    template_name = 'crm/clase/clase_confirm_delete.html'
    success_url = reverse_lazy('crm:index_clase')



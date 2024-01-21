from django.urls import path
from .views import calendar_template, registrar_asistencia, upload_file_list_view, Index

app_name = 'main'

urlpatterns = [
    path('', Index.as_view(), name='index'),
    path('asistencias', registrar_asistencia, name='registrar_asistencias'),
    path('calendario', calendar_template, name='calendario'),
    # path('', upload_file_list_view, name='form_file_list')
]

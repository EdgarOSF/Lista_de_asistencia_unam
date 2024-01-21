from django.contrib import admin
from .models import Alumno, Clase, Archivo_Lista, Ponderacion, Asistencia


admin.site.register(Alumno)
admin.site.register(Clase)
admin.site.register(Archivo_Lista)
admin.site.register(Ponderacion)
admin.site.register(Asistencia)

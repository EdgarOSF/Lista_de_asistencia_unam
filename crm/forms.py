from django import forms

from listaDeAsistenciaApp.models import Alumno, Clase


class AlumnoForm(forms.ModelForm):
    class Meta:
        model = Alumno
        fields = ('nombre', 'email')
        labels = {
            'nombre': 'Nombre del alumno', 
            'email': 'Email'
        }


class ClaseForm(forms.ModelForm):
    class Meta:
        model = Clase
        fields = ('fecha',)
        labels = {
            'fecha': 'Fecha de la clase'
        }
        widgets = {
            'fecha': forms.TextInput( attrs={ 'placeholder': 'dd/mm/yyyy', 'type': 'date' } ),
        }


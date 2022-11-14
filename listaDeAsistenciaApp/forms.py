from django import forms
from .models import Archivo_Lista


class ArchivoListaModelForm(forms.ModelForm):
    class Meta:
        model = Archivo_Lista
        fields = ['archivo']
from django import forms
from django.forms import widgets
from .models import *


class FormularioAlumnos(forms.ModelForm):
    class Meta:
        model =alumno
        fields ='__all__'
        widgets ={'fecha_nacimiento': forms.DateInput(attrs={'type': 'date'})}

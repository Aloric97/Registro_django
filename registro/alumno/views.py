from django.shortcuts import render
from django.http import HttpRequest
from .forms import *

class formulario(HttpRequest):


    def index(request):
        alumno= FormularioAlumnos()
        return render(request,'registro.html',{"form": alumno})
    

    def procesar(request):
        alumno=FormularioAlumnos(request.POST)

        if alumno.is_valid():
            alumno.save()
            alumno=FormularioAlumnos()
        
        return render(request,'registro.html',{"form":alumno, "mensaje": 'ok'})



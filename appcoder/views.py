from django.shortcuts import render
from .models import Curso
from django.http import HttpResponse
from .forms import CrearCursoForm, CrearEstudianteForm, CrearProfesorForm
from django.http import HttpResponseRedirect

# Create your views here.

def crear_curso(request):
    if request.method == 'POST':
        form = CrearCursoForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')  # replace with your success URL
    else:
        form = CrearCursoForm()
    return render(request, 'crear_curso.html', {'form': form})

def crear_estudiante(request):
    if request.method == 'POST':
        form = CrearEstudianteForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/appcoder')  # replace with your success URL
    else:
        form = CrearEstudianteForm()
    return render(request, 'crear_estudiante.html', {'form': form})

def crear_profesor(request):
    if request.method == 'POST':
        form = CrearProfesorForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/appcoder')  # replace with your success URL
    else:
        form = CrearProfesorForm()
    return render(request, 'crear_profesor.html', {'form': form})



def listar_cursos(request):
   cursos_list = Curso.objects.all()
   print(cursos_list[1].nombre)
   return render(request, 'cursos.html', {'cursos': cursos_list})

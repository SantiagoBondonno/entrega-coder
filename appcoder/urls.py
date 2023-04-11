from django.urls import path
from .views import *

urlpatterns = [
 path('crear-curso', crear_curso, name="crear_cursos"),
 path('inscribir-estudiante', crear_estudiante, name="crear_estudiante"),
 path('crear-profesor', crear_profesor, name="crear_profesor"),


 path("cursos", listar_cursos, name="listar_cursos"),
 #path("estudiantes", cursos, name="cursos"),
 #path("profesores", cursos, name="cursos"),

 path("", listar_cursos, name="cursos")

]
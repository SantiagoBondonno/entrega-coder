from django import forms
 
from .models import Curso, Estudiante, Profesores
 
class CrearCursoForm(forms.ModelForm):
    class Meta:
        model = Curso
        fields = "__all__"

class CrearEstudianteForm(forms.ModelForm):
    class Meta:
        model = Estudiante
        fields = "__all__"

class CrearProfesorForm(forms.ModelForm):
    class Meta:
        model = Profesores
        fields = "__all__"

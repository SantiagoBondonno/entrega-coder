from django.forms import ModelForm
from django.contrib.auth.models import User
from .models import Post

class CrearPostForm(ModelForm):
    class Meta:
        model = Post
        fields = ['titulo', 'contenido']

class LoginForm(ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password']

class CrearUsuarioForm(ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password']
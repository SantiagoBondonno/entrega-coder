from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth import logout
from django.contrib.auth import login as auth_login
from .models import Post
from .forms import CrearPostForm, LoginForm, CrearUsuarioForm
from django.utils import timezone


# Create your views here.
def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def ver_posts(request):
    if not request.user.is_authenticated:
        print("Usuario no autenticado")
        return HttpResponseRedirect("/login")
    posts = Post.objects.all()
    return render(request, 'posts.html', {'posts': posts})

def crear_usuarios(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        #create the user
        user = User.objects.create_user(username, '', password)
        user.save()
        return HttpResponseRedirect("/")
    else:
        form = CrearUsuarioForm()
        return render(request, 'crear_usuarios.html', {'form': form})

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)
        if user is not None:
            print("Usuario autenticado")
            auth_login(request, user)
            return HttpResponseRedirect("/posts")
        else:
            print("Usuario no autenticado")
            return HttpResponseRedirect("/login", {'error': 'Usuario o contraseña incorrectos'})

    else:
        form = LoginForm()
        return render(request, 'login.html', {'form': form})
    

def logout_view(request):
    logout(request)
    return HttpResponseRedirect("/")


def crear_post(request):
    #check if logged in
    if not request.user.is_authenticated:
        return HttpResponseRedirect("/login")
    if request.method == 'POST':
        titulo = request.POST['titulo']
        contenido = request.POST['contenido']
        #get the user
        autor = request.user
        #fecha
        fecha = timezone.now()

        post = Post(titulo=titulo, contenido=contenido, autor=autor, fecha=fecha)
        post.save()
        return HttpResponseRedirect("/posts")
    
    else:
        form = CrearPostForm()
        return render(request, 'crear_post.html', {'form': form})

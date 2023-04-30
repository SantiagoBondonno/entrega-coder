from django.urls import path

from . import views

urlpatterns = [
    path("", views.ver_posts, name="ver_posts"),
    path("posts", views.ver_posts, name="ver_posts"),
    path("crear-usuarios", views.crear_usuarios, name="crear_usuarios"),
    path("login", views.login, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("crear-post", views.crear_post, name="crear_post"),

]
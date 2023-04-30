from django.db import models
#import the user model
from django.contrib.auth.models import User


class Post(models.Model):
    titulo = models.CharField(max_length=200)
    fecha = models.DateTimeField("date published")
    contenido = models.TextField(max_length=2000)
    autor = models.ForeignKey(User, on_delete=models.CASCADE)

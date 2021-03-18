from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

# from django.conf import settings

class AppUser(models.Model):
    nombre = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    enviarnotificacion = models.BooleanField(default=True)
    token = models.CharField(max_length=200, unique=True)
    fecha = models.DateField(auto_now=True)

    def __str__(self):
        ret = self.nombre
        return ret


class Comentarios(models.Model):
    fecha = models.DateTimeField(auto_now=True)
    nombre = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    telefono = models.CharField(max_length=20)
    mensaje = models.TextField()
    motivo = models.CharField(max_length=50)
    atendido = models.BooleanField(default=False)

    class Meta:
        ordering = ['-nombre']

    def __str__(self):
        ret = self.nombre
        return ret


class Clasificacion(models.Model):
    nombre = models.CharField(max_length=100)

    class Meta:
        ordering = ['-nombre']

    def __str__(self):
        ret = self.nombre
        return ret


class Perfil(models.Model):
    nombre = models.CharField(max_length=200, null=True, blank=True)
    titulo = models.CharField(max_length=50, default='Sr(a)')
    foto = models.ImageField(upload_to='img')
    nacimiento = models.DateField(null=True, blank=True)
    biografia = models.TextField()

    class Meta:
        ordering = ['-nombre']

    def __str__(self):
        ret = self.nombre
        return ret


class Post(models.Model):
    titulo = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True)
    resumen = models.TextField()
    contenido = models.TextField()
    esnoticia = models.BooleanField(default=True)
    espromocion = models.BooleanField(default=False)
    publicado = models.BooleanField(default=True)
    creado = models.DateTimeField(auto_now=True)
    clasificacion = models.ForeignKey(Clasificacion, related_name='clasificacion', on_delete=models.CASCADE)
    referencia = models.CharField(max_length=200)
    image = models.ImageField(upload_to='img')
    #usuariocaptura = models.ForeignKey(Perfil, related_name='usuariocaptura', on_delete=models.CASCADE)

    class Meta:
        ordering = ['-creado']


    def get_absolute_url(self):
        return reverse('meriland.views.post', args=[self.slug])


    def __str__(self):
        ret = self.titulo
        return ret


from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    foto = models.ImageField(upload_to='img')
    nacimiento = models.DateField(null=True, blank=True)
    biografia = models.TextField()


class Comentarios(models.Model):
    fecha = models.DateTimeField(auto_now=True)
    nombre = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    telefono = models.CharField(max_length=20)
    mensaje = models.TextField()
    motivo = models.CharField(max_length=50)
    atendido = models.BooleanField(default=False)
    recaptcha = models.BooleanField(default=True)

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


class Post(models.Model):
    titulo = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True)
    resumen = models.TextField()
    contenido = models.TextField()
    esnoticia = models.BooleanField(default=True)
    espromocion = models.BooleanField(default=False)
    publicado = models.BooleanField(default=True)
    creado = models.DateTimeField(auto_now=True)
    clasificacion = models.ForeignKey(Clasificacion, on_delete=models.CASCADE)
    referencia = models.CharField(max_length=200)
    image = models.ImageField(upload_to='img')
    autor = models.ForeignKey(User, related_name='autor', on_delete=models.CASCADE, default=1)

    class Meta:
        ordering = ['-creado']


    def get_absolute_url(self):
        return reverse('meriland.views.post', args=[self.slug])


    def __str__(self):
        ret = self.titulo
        return ret


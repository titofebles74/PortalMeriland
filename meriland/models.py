from django.db import models
from django.urls import reverse


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
    resumen = models.CharField(max_length=300)
    contenido = models.TextField()
    publicado = models.BooleanField(default=True)
    creado = models.DateTimeField(auto_now=True)
    clasificacion = models.ForeignKey(Clasificacion, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='img')

    class Meta:
        ordering = ['-creado']


    def get_absolute_url(self):
        return reverse('meriland.views.post', args=[self.slug])


    def __str__(self):
        ret = self.titulo
        return ret


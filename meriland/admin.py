from django.contrib import admin
from .models import Post, Clasificacion, Comentarios

class ClasificacionAdmin(admin.ModelAdmin):
    # a list of displayed columns name.
    list_display = ['nombre']


class PostAdmin(admin.ModelAdmin):
    list_display = ['titulo', 'resumen', 'publicado']


class ComentariosAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'fecha', 'email', 'telefono', 'motivo']


# Register your models here.
admin.site.register(Post, PostAdmin)
admin.site.register(Clasificacion, ClasificacionAdmin)
admin.site.register(Comentarios, ComentariosAdmin)
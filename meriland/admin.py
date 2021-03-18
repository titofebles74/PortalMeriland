from django.contrib import admin
from .models import Clasificacion, Comentarios, AppUser, Post, Perfil

class ClasificacionAdmin(admin.ModelAdmin):
    # a list of displayed columns name.
    list_display = ['nombre']


class ComentariosAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'fecha', 'email', 'telefono', 'motivo']


class AppUserAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'email', 'enviarnotificacion']


class PostAdmin(admin.ModelAdmin):
    list_display = ['titulo', 'resumen', 'esnoticia', 'publicado']


class PerfilAdmin(admin.ModelAdmin):
    list_display = ['titulo', 'foto', 'nacimiento', 'biografia']


# Register your models here.
admin.site.register(Clasificacion, ClasificacionAdmin)
admin.site.register(Comentarios, ComentariosAdmin)
admin.site.register(AppUser, AppUserAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(Perfil, PerfilAdmin)
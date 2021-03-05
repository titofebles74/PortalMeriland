from django.contrib import admin
from .models import Post, Clasificacion, Comentarios, Profile, AppUser

class ClasificacionAdmin(admin.ModelAdmin):
    # a list of displayed columns name.
    list_display = ['nombre']


class PostAdmin(admin.ModelAdmin):
    list_display = ['titulo', 'resumen', 'esnoticia', 'publicado']


class ComentariosAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'fecha', 'email', 'telefono', 'motivo']


class ProfileAdmin(admin.ModelAdmin):
    list_display = ['foto', 'nacimiento', 'biografia']


class AppUserAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'email', 'enviarnotificacion']

# Register your models here.
admin.site.register(Post, PostAdmin)
admin.site.register(Clasificacion, ClasificacionAdmin)
admin.site.register(Comentarios, ComentariosAdmin)
admin.site.register(Profile, ProfileAdmin)
admin.site.register(AppUser, AppUserAdmin)
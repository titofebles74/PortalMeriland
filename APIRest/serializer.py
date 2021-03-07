'''
from rest_framework import serializers
from meriland.models import Post, Clasificacion, Comentarios


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = [{'Data': {'titulo', 'resumen', 'contenido', 'image', 'clasificacion', 'slug'}}]


class ClasificacionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Clasificacion
        fields = ['id', 'nombre']


class ComentariosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comentarios
        fields = ['fecha', 'nombre', 'email', 'telefono', 'mensaje', 'motivo', 'atendido']

'''
#otro codigo

from django.contrib.auth.models import User, Group
from meriland.models import Post, Clasificacion, Profile, Comentarios, AppUser
from rest_framework import serializers


class AppUserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = AppUser
        fields = ['id', 'nombre', 'email', 'enviarnotificacion', 'token', 'fecha']


class ProfileSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Profile
        fields = ['foto', 'biografia', 'nacimiento', 'user']


class UserSerializer(serializers.HyperlinkedModelSerializer):
    profile = ProfileSerializer(read_only=True)

    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'first_name', 'last_name', 'profile']


class ComentariosSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Comentarios
        fields = ['fecha', 'nombre', 'email', 'telefono', 'mensaje', 'motivo', 'atendido']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']


class ClasificacionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Clasificacion
        fields = ['id', 'nombre']


class PostUserSerializer(serializers.HyperlinkedModelSerializer):
    autor = UserSerializer(read_only=True)

    class Meta:
        model = Post
        fields = ['id', 'titulo', 'slug', 'resumen', 'contenido', 'publicado', 'creado', 'clasificacion', 'referencia', 'image', 'autor']
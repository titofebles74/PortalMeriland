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
from meriland.models import Post, Clasificacion
from rest_framework import serializers

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups', 'first_name', 'last_name']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']


class PostSerializer(serializers.HyperlinkedModelSerializer):
    autor = serializers.StringRelatedField(many=False)

    class Meta:
        model = Post
        fields = ['titulo', 'slug', 'resumen', 'contenido', 'publicado', 'creado', 'clasificacion', 'referencia', 'image', 'autor']


class ClasificacionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Clasificacion
        fields = ['id', 'nombre']


class PostUserSerializer(serializers.HyperlinkedModelSerializer):
    autor = UserSerializer(read_only=True)

    class Meta:
        model = Post
        fields = ['titulo', 'slug', 'resumen', 'contenido', 'publicado', 'creado', 'clasificacion', 'referencia', 'image', 'autor']
from django.shortcuts import render
from rest_framework import generics
from meriland.models import Post, Clasificacion
from .serializer import PostSerializer, ClasificacionSerializer


class PostList(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class ClasificacionList(generics.ListCreateAPIView):
    queryset = Clasificacion.objects.all()
    serializer_class = ClasificacionSerializer


'''
# Importamos las tablas que queremos ver Primero del sistema
from django.contrib.auth.models import User, Group
# Ahora los que creamos
from meriland.models import Post, Clasificacion

# Ahora serializer
from APIRest.serializer import UserSerializer, GroupSerializer, PostSerializer, ClasificacionSerializer

# importamos librearias de rest_framework
from rest_framework import viewsets
from rest_framework import permissions

# Verificar esta opcion
# from rest_framework import generics


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticated]


class ClasificacionViewSet(viewsets.ModelViewSet):
    queryset = Clasificacion.objects.all()
    serializer_class = ClasificacionSerializer
    permission_classes = [permissions.IsAuthenticated]


'''

'''
from rest_framework import generics, status
from rest_framework.views import APIView
from rest_framework.response import Response

from meriland.models import Post, Clasificacion, Comentarios
from .serializer import PostSerializer, ClasificacionSerializer, ComentariosSerializer

from rest_framework.parsers import JSONParser


class PostList(generics.ListCreateAPIView):
    queryset = Post.objects.filter(publicado=True)[:6]
    serializer_class = PostSerializer



class ClasificacionList(generics.ListCreateAPIView):
    queryset = Clasificacion.objects.all()
    serializer_class = ClasificacionSerializer


class ComentariosList(generics.ListCreateAPIView):
    queryset = Comentarios.objects.filter(atendido=False)
    serializer_class = ComentariosSerializer


class logout(APIView):
    def get(self, request, format=None):
        request.user.auth_token.delete()
        logout(request)
        return Response(status=status.HTTP_200_OK)
'''

# otro Codigo
# Importamos las tablas que queremos ver Primero del sistema
from django.contrib.auth import logout
from django.contrib.auth.models import User, Group
# Ahora los que creamos

from meriland.models import Clasificacion, Comentarios, AppUser, Perfil, Post

# Ahora serializer
from APIRest.serializer import UserSerializer, GroupSerializer, ClasificacionSerializer, ComentariosSerializer, AppUserSerializer, NotificacionSerializer, ProfileSerializer, PostUserSerializer

# importamos librearias de rest_framework
from rest_framework import viewsets
from rest_framework import permissions


class SendNotificacionViewSet(viewsets.ModelViewSet):
    serializer_class = NotificacionSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        titulo = self.request.query_params.get('titulo')
        mensaje = self.request.query_params.get('titulo')
        pantalla = self.request.query_params.get('titulo')
        return NotificacionSerializer.sendNotificacon(self, titulo, mensaje, pantalla)


class AppUserViewSet(viewsets.ModelViewSet):
    queryset = AppUser.objects.all()
    serializer_class = AppUserSerializer
    permission_classes = [permissions.IsAuthenticated]


class AppUserFiltroViewSet(viewsets.ModelViewSet):
    queryset = AppUser.objects.all()
    serializer_class = AppUserSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        token = self.request.query_params.get('token')
        return AppUser.objects.filter(token=token)


class ComentariosViewSet(viewsets.ModelViewSet):
    queryset = Comentarios.objects.all()
    serializer_class = ComentariosSerializer
    permission_classes = [permissions.IsAuthenticated]


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


class ClasificacionViewSet(viewsets.ModelViewSet):
    queryset = Clasificacion.objects.all()
    serializer_class = ClasificacionSerializer
    permission_classes = [permissions.IsAuthenticated]


class PostUserViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.filter(publicado=True, esnoticia=True).order_by('id').reverse()[:6]
    serializer_class = PostUserSerializer
    permission_classes = [permissions.IsAuthenticated]


class PostUserClasificacionViewSet(viewsets.ModelViewSet):
    # filter(publicado=True, clasificacion=2)[:6]
    queryset = Post.objects.all()
    serializer_class = PostUserSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        clasificacion = self.request.query_params.get('clasificacion')
        return Post.objects.filter(publicado=True, clasificacion=clasificacion).order_by('id').reverse()[:6]


class ProfileViewSet(viewsets.ModelViewSet):
    queryset = Perfil.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = [permissions.IsAuthenticated]


'''
class Logout(APIView):
    def get(self, request, format = None):
        # simply delete the token to force a login
        request.user.auth_token.delete()
        logout(request)
        return Response(status=status.HTTP_200_OK)
'''
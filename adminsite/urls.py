"""adminsite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path

from rest_framework import routers
from rest_framework.authtoken import views

from APIRest import views as APIRest
from meriland import views as blog

from django.conf import settings
from django.conf.urls.static import static

'''
router = routers.DefaultRouter()
router.register(r'users', APIRest.UserViewSet)
router.register(r'groups', APIRest.GroupViewSet)
router.register(r'posts', APIRest.PostViewSet)
router.register(r'clasificaciones', APIRest.ClasificacionViewSet)
'''

# path('api/', include(router.urls)),
urlpatterns = [
    path('api/1.0/', include(('APIRest.urls', 'APIRest'))),
    path('api_generate_token/', views.obtain_auth_token),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('', blog.index),
    path('quienessomos/', blog.quienessomos),
    path('avisoprivacidad', blog.avisoprivacidad),
    path('contacto/', blog.contacto),
    path('post/<slug>', blog.post),
    path('noticia/<clasificacion>', blog.filtronoticia),
    path('todaslasnoticias/', blog.todaslasnoticias),
    path('dondeestamos/', blog.dondeestamos),
    path('admin/', admin.site.urls),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

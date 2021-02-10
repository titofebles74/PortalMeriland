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
from APIRest import views as APIRest
from meriland import views as blog

from django.conf import settings
from django.conf.urls.static import static

router = routers.DefaultRouter()
router.register(r'users', APIRest.UserViewSet)
router.register(r'groups', APIRest.GroupViewSet)
router.register(r'posts', APIRest.PostViewSet)
router.register(r'clasificaciones', APIRest.ClasificacionViewSet)


urlpatterns = [
    path('API/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('', blog.index),
    path('contacto/', blog.contacto),
    path('post/<slug>', blog.post),
    path('admin/', admin.site.urls),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


from django.urls import path
from .views import PostList, ClasificacionList

urlpatterns = [
    path('post/', PostList.as_view(), name='post_list'),
    path('clasificacion/', ClasificacionList.as_view(), name='clasificacion_list'),
]
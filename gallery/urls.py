from django.urls import path
from gallery.views import *

urlpatterns = [
    path('', index),
    path('imagem/', imagem, name = 'imagem'),
]
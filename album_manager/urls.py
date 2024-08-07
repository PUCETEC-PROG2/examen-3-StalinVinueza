# Ingresar tus URLs de la app aquí
from django.urls import path

from . import views

app_name = 'album_manager'
urlpatterns = [
    path("", views.index, name="index"),
  

]
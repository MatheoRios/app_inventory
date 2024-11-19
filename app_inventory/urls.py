from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
     path('catalogo/', views.vw_catalogos,name="catalogo"),

    
]
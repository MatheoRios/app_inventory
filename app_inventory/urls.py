from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
     path('states/', views.vw_states,name="states"),
         #path('states_set/<int:states_id>/<str:name_states>/', views.vw_states_set)
         
]
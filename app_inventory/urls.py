from django.urls import path
from . import views

urlpatterns = [
     #url  vista genericas
    path('index', views.index),
     path('success/', views.success_view, name='success_view'),
    #url  vista genericas
     
     
    #url  vista vw_departments
    path('departments/', views.vw_departments,name="departments"),
    path('register/', views.register_department, name='register_department'),
    path('edit_department/<int:id>/', views.edit_department, name='edit_department'),
    #url  vista vw_departments
    
    
    
    
   

         
]
from django.urls import path, include
from AppCoder.views import *



urlpatterns = [
    
    path('inicio/', inicio, name="AppCoder-inicio"),   
    path('galeria/', creacion_Galeria, name="AppCoder-Galeria"),
    path('taller/', creacion_Taller, name="AppCoder-Taller"),    
    path('contacto/', creacion_Contacto, name="AppCoder-Contacto"),
    path('buscar/', buscar_alumnos, name="AppCoder-busquedaAlumnos"),
    
    

    
]



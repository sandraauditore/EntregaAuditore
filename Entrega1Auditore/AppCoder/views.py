
from urllib import request
from AppCoder.forms import ContactoFormulario, GaleriaFormulario, TallerFormulario
from AppCoder.models import Contacto, Galeria, Taller
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.



def inicio(request):
    return render(request, "AppCoder/index.html")


def creacion_Galeria(request):

    if request.method == "POST":
        formulario = GaleriaFormulario(request.POST)
        if formulario.is_valid():
           data = formulario.cleaned_data
           galeria = Galeria(Nombre=data["Nombre"], Descripcion=data["Descripcion"], Imagen=data["Imagen"] )
           galeria.save()
    formulario = GaleriaFormulario()
    return render(request, "AppCoder/Galeria.html", {"formulario": formulario})



def creacion_Taller(request):

   if request.method == "POST":
       formulario = TallerFormulario(request.POST)
       if formulario.is_valid():
          data = formulario.cleaned_data
          taller = Taller(Nombre=data["Nombre"], Apellido=data["Apellido"], Email=data["Email"])
          taller.save()
   formulario = TallerFormulario()
   return render(request, "AppCoder/Taller.html", {"formulario": formulario})





def creacion_Contacto(request):

    if request.method == "POST":
        formulario = ContactoFormulario(request.POST)
        if formulario.is_valid():
            data = formulario.cleaned_data
            contacto = Contacto(Nombre=data["Nombre"], Email=data["Email"], Mensaje=data["Mensaje"])
            contacto.save()
    formulario = ContactoFormulario()
    return render(request, "AppCoder/Contacto.html", {"formulario": formulario})


     

def buscar_alumnos(request):
    if request.GET:
      estudiantes = Taller.objects.filter(Nombre__icontains=request.GET["nombre_alumno"])
      return render(request, "AppCoder/busquedaAlumnos.html", {"listado_alumnos": estudiantes}) 
    return render(request, "AppCoder/busquedaAlumnos.html", {"listado_alumnos": []}) 
       
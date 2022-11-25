from django import forms


class ContactoFormulario(forms.Form):
    
    Nombre = forms.CharField()
    Email = forms.EmailField()
    Mensaje = forms.CharField()

class GaleriaFormulario(forms.Form):
    
    Nombre = forms.CharField()
    Descripcion = forms.CharField()
    Imagen = forms.ImageField()
    

class TallerFormulario(forms.Form):
    
    Nombre = forms.CharField()
    Apellido = forms.CharField()
    Email = forms.EmailField()

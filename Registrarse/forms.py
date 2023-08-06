
from django import forms

class FormularioRegistro(forms.Form):

     nombre =forms.CharField(label='Nombre', required=True, max_length=100)
     apellidos = forms.CharField(label='Apellido', required=True, max_length=100)
     email = forms.CharField(label='Email', required=True)
     contraseña = forms.CharField(label='Contraseña', widget=forms.PasswordInput,required=True, max_length=100)
    
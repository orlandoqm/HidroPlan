
from django import forms

from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class actualizaForm(UserCreationForm):
    username=forms.CharField(label="Nombre de usuario")
    first_name = forms.CharField(label='Nombre')
    last_name = forms.CharField(label='Apellidos')
    email = forms.EmailField()
    password1 = forms.CharField(label='Contraseña nueva' ,widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirma contraseña nueva', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'first_name','last_name','email','password1','password1']
        help_texts = {k:"" for k in fields}

'''class FormularioDatos(forms.Form):

     nombre =forms.CharField(label='Nombre', required=True, max_length=100)
     apellidos = forms.CharField(label='Apellido', required=True, max_length=100)
     email = forms.CharField(label='Email', required=True)
     contraseña = forms.CharField(label='Contraseña', widget=forms.PasswordInput,required=True, max_length=100)
    '''
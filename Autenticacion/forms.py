from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm


class UserRegisterForm(UserCreationForm):
    first_name = forms.CharField(label='Nombre')
    last_name = forms.CharField(label='Apellidos')
    email = forms.EmailField()
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirma contraseña', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'first_name','last_name','email','password1','password2']
        help_texts = {k:"" for k in fields}

class CustomLoginForm(AuthenticationForm):
    username = forms.CharField(
        label="Nombre de usuario",
        widget=forms.TextInput(attrs={'class': 'form-control'}),
    )
    password = forms.CharField(
        label="Contraseña",
        widget=forms.PasswordInput(attrs={'class': 'form-control'}),
    )
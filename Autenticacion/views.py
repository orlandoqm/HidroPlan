from django.shortcuts import render,redirect
from django.views.generic import View
from django.contrib.auth import login,logout, authenticate
from django.contrib import messages

from django.contrib.auth.forms import UserCreationForm,AuthenticationForm

from .forms import UserRegisterForm

# Create your views here.
class vistaRegistro(View):

    def get(self,request):
        form= UserRegisterForm()
        
        return render(request,'registro/registro.html',{"form":form})
    
    def post(self, request):
        form = UserRegisterForm(request.POST)

        if form.is_valid():
           email=form.cleaned_data.get("email")
           print("--->",email)

          

           usuario= form.save()
           login(request, usuario)
           
           return redirect('home')
        
        else:
            print("no se valido el formulario!!!")
            for msg in form.error_messages:
                messages.error(request, form.error_messages[msg])
            
            return render(request,"registro/registro.html",{"form":form})
        
def cerrarSesion(request):
    logout(request)

    return redirect('home')

def iniciarSesion(request):

    if request.method=="POST":
        form=AuthenticationForm(request,data=request.POST)
        if form.is_valid():
            nombreUsuario=form.cleaned_data.get("username")
            contrasena=form.cleaned_data.get("password")
            

            print("------->",nombreUsuario)
            print("------->",contrasena)
            usuario=authenticate(username=nombreUsuario, password=contrasena)
            if usuario is not None:
                login(request,usuario)
                return redirect('home')
            else:
                messages.error(request,"Usuario no válido")

        else:
            messages.error(request,"Datos incorrectos")
    form=AuthenticationForm()
    return render(request,"Login/login.html",{"form":form})

                

    



    
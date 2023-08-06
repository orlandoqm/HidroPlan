
from django.shortcuts import redirect, render
from django.views.generic import View
from .forms import actualizaForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages

# Create your views here.

class vistaActualiza(View):

    def get(self,request):
        form= actualizaForm()
        datosPerfil=obtenerDatosUsuario(request)
        form = actualizaForm( initial={"username":datosPerfil["nombreusuario"],
                                             "first_name":"Orlando",
                                             "last_name":"Quiroga Maldonado",
                                             "email":datosPerfil["correo"]})
        
        return render(request,'DatosPersonales/datosPersonales.html',{"datos":form})
    
    def post(self, request):
        form = actualizaForm(request.POST)
        print("metodo post--->")
        if form.is_valid():
         id_usuario = request.user.id
         nombreusuario=request.POST.get("username")
         nombre=request.POST.get("first_name")
         apellido=request.POST.get("last_name")
         correo=request.POST.get("email")
         nuevaContrasena=request.POST.get("password1")
         print(nombre)

         
         user= User.objects.get(id=id_usuario)
         user.username=nombreusuario
         user.first_name=nombre
         user.last_name=apellido
         user.email=correo
          
         user.save()
        #no hizo la actualizacion
        
         print("Actualizacion  exitosa!!")
           
         return redirect('home')
        
        else:
            print("no se valido el formulario!!!")
            for msg in form.error_messages:
                messages.error(request, form.error_messages[msg])

            return render(request,'DatosPersonales/datosPersonales.html',{"datos":form})

    

def DatosPersonales(request):

    datosPerfil=obtenerDatosUsuario(request)
    #print("--->",datosPerfil["correo"])

    form = actualizaForm( initial={"username":datosPerfil["nombreusuario"],
                                             "first_name":"Orlando",
                                             "last_name":"Quiroga Maldonado",
                                             "email":datosPerfil["correo"]})
    
    if request.method == "POST":
       
        id_usuario = request.user.id
        nombreusuario=request.POST.get("username")
        nombre=request.POST.get("first_name")
        apellido=request.POST.get("last_name")
        correo=request.POST.get("email")
        nuevaContrasena=request.POST.get("password1")
        print(nombre)

        print("metodo post--->")
        if form.is_valid():
         user= User.objects.get(id=id_usuario)
         user.username=nombreusuario
         user.first_name=nombre
         user.last_name=apellido
         user.email=correo

        #if user.check_password(nuevaContrasena):

        
        

         user.save()
        #no hizo la actualizacion
        
         print("Actualizacion  exitosa!!")
        else:
        
         print("no se valido el formulario!!!")
         for msg in form.error_messages:
          messages.error(request, form.error_messages[msg])

        return render(request,"DatosPersonales/datosPersonales.html",{"datos":form})
        

    return render(request,'DatosPersonales/datosPersonales.html',{"datos":form})
'''
def DatosPersonales(request):

    nombre=obtenerDatosUsuario(request)
    calculoFecha = FormularioDatos( initial={"nombre":"Orlando",
                                             "apellidos":"Quiroga Maldonado",
                                             "email":"orlando@gmail.com"})


    return render(request,'DatosPersonales/datosPersonales.html',{"datos":calculoFecha})'''

@login_required
def obtenerDatosUsuario(request):
    id_usuario = request.user.id
    nombreUsuario=request.user.username
    nombre=request.user.first_name
    apellidos=request.user.last_name
    correo=request.user.email

    datos={"idUsuario":id_usuario,"nombreusuario":nombreUsuario,
            "nombre":nombre,"apellidos":apellidos,"correo":correo}
    #print(datos)
    return datos
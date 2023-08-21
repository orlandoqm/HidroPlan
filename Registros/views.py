from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from Lechuga.models import cultivo
from Betabel.models import cultivoB
from Espinaca.models import cultivoE

from . forms import FormularioRegistro
#from.registro import 

# Create your views here.
def registro(request):
    #idU= request.POST.get("idUsuario")
   # listaLechuga=cultivo.objects.all()
    #print("id usuario--->",idU)
    
    obtener_email(request)
    id=obtener_id_usuario(request)
    listaLechuga=cultivo.objects.filter(idUsuario=id)
    listaBetabel=cultivoB.objects.filter(idUsuario=id)
    listaEspinaca=cultivoE.objects.filter(idUsuario=id)
     

    if request.method=="POST"  :
     print("METODO POST")
     botonPulsado = request.POST.get("bt")
     print("-->",botonPulsado)
     fecha=request.POST.get("fecha")
     if fecha !="":
       
      if botonPulsado=="Fecha de siembra":
      #fecha=request.POST.get("fecha")
       print("dato recibida::::",fecha)
       listaLechuga=cultivo.objects.filter(fechaSiembra=fecha)
       listaBetabel=cultivoB.objects.filter(fechaSiembra=fecha)
       listaEspinaca=cultivoE.objects.filter(fechaSiembra=fecha)
      
      else :
        print("dato recibida::::",fecha)
        listaLechuga=cultivo.objects.filter(fechaCosecha=fecha)
        listaBetabel=cultivoB.objects.filter(fechaCosecha=fecha)
        listaEspinaca=cultivoE.objects.filter(fechaCosecha=fecha)
     
      #fecha=request.POST.get("fecha")
       


     else:
       
        eliminarRegistro(request,botonPulsado,listaLechuga,listaBetabel,listaEspinaca)
      
       
    return render(request,'Registros/registros.html',{'listaLechuga':listaLechuga,"listaBetabel":listaBetabel,"listaEspinaca":listaEspinaca})


def filtrarDatos(lista,idUsuario):
  lista=cultivo.objects.filter(id=idUsuario)
  return lista
     
def eliminarRegistro(request,botonPulsado,listaLechuga,listaBetabel,listaEspinaca):

  if botonPulsado=="Eliminar registro de lechuga":
    idL=request.POST.get("eliminarLechuga")
    try:
     lechuga = cultivo.objects.get(id = idL)
     lechuga.delete()
     
     print("Registro eliminado!")
    except:
     print("El registro no existe")
   
  elif botonPulsado=="Eliminar registro de betabel":
    idB=request.POST.get("eliminarBetabel")
    try:
     betabel = cultivoB.objects.get(id = idB)
     betabel.delete()
     print("Registro eliminado!")
    except:
     print("El registro no existe")
  else:
    idE=request.POST.get("eliminarEspinaca")
    try:
      espinaca = cultivoE.objects.get(id = idE)
      espinaca.delete()
      print("Registro eliminado!")
    except:
     print("El registro no existe")
   
    

  return render(request,'Registros/registros.html',{'listaLechuga':listaLechuga,"listaBetabel":listaBetabel,"listaEspinaca":listaEspinaca})


def imprimir():
  lista=cultivo.objects.all()
  print("REGISTROS...imprimiento lista....")
  for ob in lista:
   print(ob)

@login_required
def obtener_id_usuario(request):
    id_usuario = request.user.id
    return id_usuario

@login_required
def obtener_email(request):
    email_usuario = request.user.email
    print("---->",email_usuario)
    return email_usuario
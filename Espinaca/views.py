from django.shortcuts import render, redirect
from . forms import FormularioCalculos, FormularioTabla
import datetime
from django.contrib.auth.decorators import login_required
from Espinaca.hilo import iniciarTiempo
from Espinaca.models import *

# Create your views here.


def espinaca(request):

    calculoFecha = FormularioCalculos()
    nombre = FormularioTabla()

    if request.method == "POST":  # si e
        botonPulsado = request.POST.get("bt")
        if botonPulsado == "enviar":
            print("se pulso botn enviar", botonPulsado)
            calculoFecha = FormularioCalculos(data=request.POST)

            opcion = request.POST.get("numero")
            print("------------------>", opcion)
            

            cantidadPlantas = request.POST.get("cantPlantas")
            if opcion == "1":  # seleccionado la opcion con: Fecha de siembra
                print("opcion======>", opcion)
                fechaSiembra = request.POST.get("fDs")
                cantP=request.POST.get("cantPlantas")

                print("---->FECHA I: ", fechaSiembra)

                # fechas de siembra

                stringFecha = ""+fechaSiembra

                fechaTimeSiembra = datetime.datetime.strptime(
                    stringFecha, '%Y-%m-%d')
                print("---->Fecha Conv: ", fechaTimeSiembra)

                f = calcularFechas(fechaTimeSiembra, 1)
                ph=obtenerCaracteristica("ph")
                temp=obtenerCaracteristica("temp")
                kg=(int(cantP)*300)/1000

                print(datetime.datetime.strftime(f[0], '%d-%m-%Y'))

                return render(request, 'Espinaca/espinaca.html', {'fechaSiembra': calculoFecha,
                                                                "fechasCalculadas": [datetime.datetime.strftime(f[0], '%d-%m-%Y'), datetime.datetime.strftime(f[1],
                                                                                                                                                              '%d-%m-%Y'), datetime.datetime.strftime(f[2], '%d-%m-%Y'),
                                                                                     datetime.datetime.strftime(f[3], '%d-%m-%Y'), cantidadPlantas,kg,ph,temp], 'nombre': nombre, 'bandera': ["p2"]})
            else:  # seleccionado la opcion con: Fecha de cosecha
                print("opcion======>", opcion)

                fechaCosecha = request.POST.get("fDc")
                print("---->FECHA I: ", fechaCosecha)

                stringFecha = ""+fechaCosecha
                fechaTimeSiembra = datetime.datetime.strptime(
                    stringFecha, '%Y-%m-%d')

                f = calcularFechas(fechaTimeSiembra, 2)
                print(datetime.datetime.strftime(f[0], '%d-%m-%Y'))

                return render(request, 'Espinaca/espinaca.html', {'fechaSiembra': calculoFecha,
                                                                "fechasCalculadas": [datetime.datetime.strftime(f[0], '%d-%m-%Y'), datetime.datetime.strftime(f[1],
                                                                                                                                                              '%d-%m-%Y'), datetime.datetime.strftime(f[2], '%d-%m-%Y'),
                                                                                     datetime.datetime.strftime(f[3], '%d-%m-%Y'), cantidadPlantas], 'nombre': nombre, 'bandera': ["p2"]})

        else:  # SE PULSO EL BOTON GUARDAR DATOS -LOGUEADO
            print("se pulso el boton guardar")
            # parte donde se guardara los datos en la BD

            dato = request.POST.get("fechaS")

            if (dato is not None):

                cantidadPlantas = request.POST.get("cantPlantas")
                print(cantidadPlantas)
                fecha1 = request.POST.get("fechaS")
                fecha2 = request.POST.get("fechaG")
                fecha3 = request.POST.get("fechaT")
                fecha4 = request.POST.get("fechaC")
                idUsuario = request.POST.get("idUsuario")

                print("ID USUARIO: :", idUsuario)

                fechas = str(fecha1)+"  "+str(fecha2)+" " + \
                    str(fecha3)+"  "+str(fecha4)

                print("fechas>>>>>> :", fechas)

                guardarDatos(fecha1, fecha2, fecha3, fecha4,
                             idUsuario, cantidadPlantas,request)
                return render(request, 'Espinaca/espinaca.html', {'fechaSiembra': calculoFecha, "nombre": nombre, 'bandera': ["p1"]})

            # return redirect('/Lechuga/?invalido')
    else:
        print("es un metodo GET")
        return render(request, 'Espinaca/espinaca.html', {'fechaSiembra': calculoFecha, "nombre": nombre, 'bandera': ["p1"]})

    return render(request, 'Espinaca/espinaca.html', {'fechaSiembra': calculoFecha, 'bandera': ["p2"], "nombre": nombre})


def calcularFechas(fecha, tipo):

    print("--FECHAS--")
    if tipo == 1:  # es fecha de SIEMBRA
        print(fecha)

    # se le aumenta 15 dias, lo que tarda en germinar las semilas
        fechaGerminacion = fecha + datetime.timedelta(days=15)
        fechaTrasplante = fecha + datetime.timedelta(days=35)
        fechaCosecha = fecha + datetime.timedelta(days=85)
        diccFechas = [fecha, fechaGerminacion, fechaTrasplante, fechaCosecha]
    else:  # es fecha de COSECHA

        # se le resta 85 dias a la fecha dada, para conocer la siembra
        fechaSiembra = fecha - datetime.timedelta(days=85)
        fechaGerminacion = fechaSiembra + datetime.timedelta(days=15)
        fechaTrasplante = fechaSiembra + datetime.timedelta(days=35)
        diccFechas = [fechaSiembra, fechaGerminacion, fechaTrasplante, fecha]

    return diccFechas


def guardarDatos(fecha1, fecha2, fecha3, fecha4, idUsuario, cantPlantas,request):

    # convertir las fechas en el formato adecuado antes insertar en la BD
    f1 = datetime.datetime.strptime(fecha1, '%d-%m-%Y').strftime('%Y-%m-%d')
    f2 = datetime.datetime.strptime(fecha2, '%d-%m-%Y').strftime('%Y-%m-%d')
    f3 = datetime.datetime.strptime(fecha3, '%d-%m-%Y').strftime('%Y-%m-%d')
    f4 = datetime.datetime.strptime(fecha4, '%d-%m-%Y').strftime('%Y-%m-%d')


    codigo = str(f1)
    guion = "-"

    for x in range(len(guion)):
     codigo=codigo.replace(guion[x],"")

    nombre=codigo+str(crear_claveDeRegistro(request))#nombre de usuario+fecha:20230627erick

    espinaca = cultivoE(

        nombreRegistro=nombre,
        fechaSiembra=f1,
        fechaGerminacion=f2,
        fechaTrasplante=f3,
        fechaCosecha=f4,
        cantPlantas=cantPlantas,
        kgAproxCosecha=(int(cantPlantas)*300)/1000,#cambiar valor 300
        ph="7.0",
        temperatura="27.0",
        idUsuario=idUsuario,

    )
    
    email=obtener_email(request)
    iniciarTiempo(nombre,f1,f2,f3,f4,email)
    espinaca.save()


def consultarRegistros():
    lista = cultivoE.objects.all()
    print("imprimiento lista....")
    for ob in lista:
        print(ob)


def imprimir():
    lista = cultivoE.objects.all()
    print("imprimiento lista....")
    for ob in lista:
        print(ob)


def obtenerCaracteristica(clave):

    diccRequierimientos = {'ph': "5,5 y 6,5.",
                           'temp': "20 °c",
                           'transplante': "Cuando tenga de 6 a 8 hojas y una altura aproximada de 8 cm",

                           'riego': "Cambiar solucion cada 15 días.",

                           }

    return diccRequierimientos[clave]

@login_required
def crear_claveDeRegistro(request):
   
 #en caso de incuir clace con hora
 hora_actual = datetime.datetime.now()
 claveHora= str(hora_actual.hour)+str(hora_actual.minute)+str(hora_actual.second)

 nombreUsuario = request.user.first_name
 apellidoUsuario = request.user.last_name
    #string = 'hola mundo python'

 words = apellidoUsuario.split(' ') 
 caracter = ''

 for word in words:
     caracter += word[0]
     nombreUsuario=nombreUsuario[0]+caracter
 return nombreUsuario

@login_required
def obtener_email(request):
    email_usuario = request.user.email
    print("---->",email_usuario)
    return email_usuario

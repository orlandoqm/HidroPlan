import threading
from time  import sleep
import datetime
from django.core.mail import send_mail
from django.contrib.auth.decorators import login_required
from Lechuga.models import cultivo
from Lechuga import constantesL

def ejecutarHilo(**kwargs):
    print("Ha iniciado el hilo")
    print(f'{threading.current_thread().name} {threading.get_native_id()}')
    
    f1=kwargs['fechaGerminacion']
    f2=kwargs['fechaTrasplante']
    f3=kwargs['fechaCosecha']
    correoDestino=kwargs['correo']
    nombreR=kwargs['nombre']
    
    #formateo de las fechas para que puedan compararlas "%Y-%m-%d"
    formatting = "%Y-%m-%d"
    fechaG=datetime.datetime.strptime(f1, formatting).date()
    fechaT=datetime.datetime.strptime(f2, formatting).date()
    fechaC=datetime.datetime.strptime(f3, formatting).date()

    #inicia la ejecucion de las ETAPAS
    #ciclo de TRASPLANTE
    fin=False
    diasSumados=0 #contador para simular el paso del dia
    while fin!=True:
     estadoRegistro=cultivo.objects.filter(nombreRegistro=nombreR).exists()
     fecha_actual = datetime.datetime.now().date()
     fechaA=fecha_actual + datetime.timedelta(days=diasSumados)
   
    
     print("Hilo corriendo...")
     print("FechaA: ",fechaA)
     print("Fecha G: ",fechaG)
     diasFaltantes=fechaG-fechaA #Se obtiene los dias restantes para que no verifique la fecha todo el tiempo desde el inicio
     print("Diferencias de dias: ",diasFaltantes.days)
     if estadoRegistro:
       if fechaA==fechaG:
        print("Las semillas ya estan germinadas...")
       
        enviar_correo(constantesL.asuntoGerminacion, constantesL.mensajeGerminacion,correoDestino)
        fin=True
       else:
        diasSumados+=1#contador para simular el paso del dia
        sleep(1)# 1 dia=1  segundos PRUEBA
        #tiempoDeEspera=(diasFaltantes.days*86400)+604800# Notificacion a las 7:00 am PROBAR
        # sleep(tiempoDeEspera)# 1 dia=86400 segundos PRODUCCION
     else:
       fin=True

     

     #ciclo de TRASPLANTE
     fin2=False
    while fin2!=True:
     
     estadoRegistro=cultivo.objects.filter(nombreRegistro=nombreR).exists()
     fecha_actual = datetime.datetime.now().date()
     fechaA=fecha_actual + datetime.timedelta(days=diasSumados)

     print("Trasplantes:Hilo corriendo...")
     print("FechaA: ",fechaA)
     print("Fecha T: ",fechaT)
     diasFaltantes=fechaT-fechaA #Se obtiene los dias restantes para que no verifique la fecha todo el tiempo desde el inicio
     print("Diferencias de dias: ",diasFaltantes.days)
     if estadoRegistro:
       if fechaA==fechaT:
        print("Las plantas listas para trasplantarse...")
        asunto="Las plantas estan listas para trastaplantar!!"
        mensaje="Las plantas estan listas para trastaplantar..."
        enviar_correo(constantesL.asuntoTrasplante, constantesL.mensajeTrasplante,correoDestino)
        fin2=True
       else:
        diasSumados+=1#contador para simular el paso del dia
        sleep(1)# 1 dia=1  segundos PRUEBA
     else:
      fin2=True
     
    #ciclo de COSECHA
    fin3=False
    while fin3!=True:
     estadoRegistro=cultivo.objects.filter(nombreRegistro=nombreR).exists()
     fechaA=fecha_actual + datetime.timedelta(days=diasSumados)
     fecha_actual = datetime.datetime.now().date()
     
     print("Cosecha:Hilo corriendo...")
     print("FechaA: ",fechaA)
     print("Fecha C: ",fechaC)
     diasFaltantes=fechaC-fechaA #Se obtiene los dias restantes para que no verifique la fecha todo el tiempo desde el inicio
     print("Diferencias de dias: ",diasFaltantes.days)
     if estadoRegistro:
        if fechaA==fechaC:
         print("Las plantas listas para cosecharse...")
         asunto="Las plantas estan listas para cosechar!!"
         mensaje="Las plantas estan listas para cosechar..."
         enviar_correo(constantesL.asuntoCosecha, constantesL.mensajeCosecha,correoDestino)
         fin3=True
        else:
         diasSumados+=1#contador para simular el paso del dia
         sleep(1)
     else:
       fin3=True
    
    
    print("El hilo ha terminado...")
       
    



def iniciarTiempo(nombre,fechaSiembra,fechaGerminacion,fechaTrasplante,fechaCosecha,email): 
 hilo1=threading.Thread(target=ejecutarHilo,name=nombre,kwargs={'fechaSiembra': fechaSiembra, 'fechaGerminacion': fechaGerminacion,
                                                                'fechaTrasplante':fechaTrasplante,'fechaCosecha':fechaCosecha,'correo':email,'nombre':nombre})
 hilo1.start()
 print(hilo1.is_alive)



def enviar_correo(asunto,mensaje,correoDestino):
    subject = "Lechuga: "+asunto
    message = mensaje
    from_email = 'orlandoquirogam@gmail.com'  # Aquí puede ser la misma dirección configurada en settings.py o una diferente.
    recipient_list = [correoDestino]  # Coloca la dirección de correo del destinatario aquí.

    send_mail(subject, message, from_email, recipient_list)

@login_required
def obtener_id_usuario(request):
    id_usuario = request.user.id
    return id_usuario

@login_required
def obtener_email(request):
    email_usuario = request.user.email
    print("---->",email_usuario)
    return email_usuario

def verificarRegistro(nombreR):
  estadoRegistro=cultivo.objects.filter(nombreRegistro=nombreR).exists()
  print("ESTADO::: ",estadoRegistro)
  return estadoRegistro

#hora_actual = datetime.datetime.now()
#fecha_actual = datetime.datetime.now().date() #2022-10-21
#hora_formateada = hora_actual.strftime('%H:%M')
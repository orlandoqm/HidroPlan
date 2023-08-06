from django.urls import path
from .views import vistaRegistro,cerrarSesion,iniciarSesion

urlpatterns = [

  
      path('',vistaRegistro.as_view(), name="autenticacion"),
      path('cerrarSesion',cerrarSesion, name="cerrarSesion"),
       path('iniciarSesion',iniciarSesion, name="iniciarSesion"),
       
]

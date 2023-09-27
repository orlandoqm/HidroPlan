from django.urls import path
from DatosPersonales.views import ChangePasswordView
from .import views



urlpatterns = [

  
     #path('',vistaActualiza.as_view(), name="datosPersonales"),
      # path('',views.DatosPersonales, name="datosPersonales"),
      path('',views.profile, name="datosPersonales"),
       path('cambiarContrasena',ChangePasswordView.as_view(), name="cambiarContrasena"),
        path('eliminarUsuario',views.eliminarUsuario, name="eliminarUsuario"),
       
]

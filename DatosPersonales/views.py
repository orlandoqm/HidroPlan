
from urllib import request
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.contrib.auth.views import PasswordChangeView
from django.contrib.messages.views import SuccessMessageMixin
from Autenticacion.views import cerrarSesion
from django.contrib.auth.models import User
from Betabel.models import cultivoB
from Espinaca.models import cultivoE

from Lechuga.models import cultivo

from .forms import UpdateUserForm


@login_required
def profile(request):
    if request.method == 'POST':
        user_form = UpdateUserForm(request.POST, instance=request.user)
        #profile_form = UpdateProfileForm(request.POST, request.FILES, instance=request.user.profile)

        if user_form.is_valid() :
            user_form.save()
            
            messages.success(request, 'Your profile is updated successfully')
            return redirect(to='datosPersonales')
    else:
        user_form = UpdateUserForm(instance=request.user)
        #profile_form = UpdateProfileForm(instance=request.user.profile)


    return render(request, 'DatosPersonales/datosPersonales.html', {'user_form': user_form})

class ChangePasswordView(SuccessMessageMixin, PasswordChangeView):
    template_name = 'DatosPersonales/cambiarContrasena.html'
    success_message = "Successfully Changed Your Password"
    
    success_url = reverse_lazy('cerrarSesion')


@login_required
def eliminarUsuario(request):
  id_usuario = request.user.id
  
  try:
    #elimina el usuario
    usuario_a_eliminar = User.objects.get(id=id_usuario)
    usuario_a_eliminar .delete()

    #elimina los registros del usuario eliminado
    listaLechuga=cultivo.objects.filter(idUsuario=id_usuario)
    listaLechuga.delete()
    listaBetabel=cultivoB.objects.filter(idUsuario=id_usuario)
    listaBetabel.delete()
    listaEspinaca=cultivoE.objects.filter(idUsuario=id_usuario)
    listaEspinaca.delete()

    print("Se ha eliminado el usuario!!",id_usuario)
  except User.DoesNotExist:
     print("Usuario no existe")
  
  
  #cerrarSesion(request)

  return cerrarSesion(request)


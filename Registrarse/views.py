from django.shortcuts import render
from . forms import FormularioRegistro
#from.registro import 

# Create your views here.
def registro(request):

    registro= FormularioRegistro()

    return render(request,'registro/registrox.html',{'registroForm':registro})

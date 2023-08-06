from django.urls import path
from . import views



urlpatterns = [

  
     # path('',vistaRegistro.as_view, name="betabel"),
       path('',views.betabel, name="betabel"),
       
]

from django.urls import path
from HidroPlanApp import views

urlpatterns = [

    path('', views.home, name='home'),
    # path('lechuga',views.lechuga, name="lechuga"),
   # path('betabel', views.betabel, name="betabel"),
    #path('espinaca', views.espinaca, name="espinaca"),

    path('personales', views.personales, name="personales"),
]

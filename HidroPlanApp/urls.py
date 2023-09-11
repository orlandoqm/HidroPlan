from django.urls import path
from HidroPlanApp import views

urlpatterns = [

    path('', views.home, name='home'),
   
]

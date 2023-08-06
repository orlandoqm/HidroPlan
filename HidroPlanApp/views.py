from django.shortcuts import render, HttpResponse

# Create your views here.

def home(request):
    
    return render(request,'HidroPlanApp/home.html')

#def lechuga(request):
 #  return render(request,'HidroPlanApp/lechuga.html')

#def betabel(request):
  # return render(request,'HidroPlanApp/betabel.html')

#def espinaca(request):
 #return render(request,'HidroPlanApp/espinaca.html')


def personales(request):
    
    return render(request,'HidroPlanApp/personales.html')
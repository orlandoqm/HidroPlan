
from django import forms

class FormularioCalculos(forms.Form):

     fechaSm =forms.DateField( label='Fecha', required=True,widget=forms.SelectDateWidget(years=range(2023,2030),attrs={
                                        'class':'form-control',
                                    }))
     
     cantidadPlantas = forms.IntegerField(min_value=2)
     fechaCosecha = forms.DateField(widget=forms.SelectDateWidget(years=range(2023,2030),attrs={
                                        'class':'form-control',
                                    }))
     
class FormularioTabla(forms.Form):
      nombre = forms.CharField(label="nombre", max_length=100)    

         
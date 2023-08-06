from django.db import models

# Create your models here.
from django.db import models

# Create your models here.
class cultivoE(models.Model):
    fechaSiembra=models.DateField()
    fechaGerminacion=models.DateField()
    fechaTrasplante=models.DateField()
    fechaCosecha=models.DateField()
    cantPlantas=models.IntegerField()
    kgAproxCosecha= models.DecimalField(max_digits=5, decimal_places=2)
    ph =models.CharField(max_length=50) 
    temperatura=models.CharField(max_length=50)
    idUsuario=models.IntegerField()

    class Meta:
       # dt_table="Lechuga"
        verbose_name="registro"
        verbose_name_plural="registros"
    
    def _str_(self):
        return self.fechaCosecha

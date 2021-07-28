from django.db import models

class alumno(models.Model):
    nombre = models.CharField(max_length=30)
    apellido= models.CharField(max_length=30)
    telefono= models.CharField(max_length=12, null=True)
    fecha_nacimiento=models.DateField(auto_now_add=True, null=True)
    codigo=models.IntegerField()


    class Meta:
        db_table ='alumno'
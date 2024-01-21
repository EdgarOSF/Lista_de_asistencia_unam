from django.db import models
from django.urls import reverse


class Alumno(models.Model):
    nombre = models.CharField(max_length=200)
    email = models.CharField(max_length=150, null=True, blank=True)

    def __str__(self):
        return f'{self.nombre} - {self.email}'
    
    def get_absolute_url(self):
        return reverse("crm:alumno_detail", kwargs={"pk": self.pk})
    
    def get_asistencias(self):
        return self.asistencias.count()
    
   
class Clase(models.Model):
    fecha = models.DateField()

    def __str__(self):
        return str(self.fecha)
    
    def get_absolute_url(self):
        return reverse("crm:clase_detail", kwargs={"pk": self.pk})
    

class Ponderacion(models.Model):
    asistencia = models.IntegerField(null=True, blank=True, default= 0)
    exposicion =  models.IntegerField(null=True, blank=True, default= 0)
    participacion = models.IntegerField(null=True, blank=True, default= 0)
    noticia = models.IntegerField(null=True, blank=True, default=0)
    fk_alumno = models.ForeignKey(Alumno, on_delete=models.CASCADE, related_name='ponderaciones')

    
class Asistencia(models.Model):
    fk_clase = models.ForeignKey(Clase, on_delete=models.CASCADE)
    fk_alumno = models.ForeignKey(Alumno, on_delete=models.CASCADE, related_name='asistencias')    


class Archivo_Lista(models.Model):
    archivo = models.FileField(upload_to='csv')

    def __str__(self) -> str:
        return self.archivo.name

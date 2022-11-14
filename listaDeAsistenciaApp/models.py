from django.db import models


class Ponderacion(models.Model):
    VALUES_CHOICES = (
        (0, 'No'),
        (1, 'Si')
    )
    asistencia = models.IntegerField(choices=VALUES_CHOICES)
    exposicion =  models.IntegerField(choices=VALUES_CHOICES)
    participacion = models.IntegerField(choices=VALUES_CHOICES)
    noticia = models.IntegerField(choices=VALUES_CHOICES)


class Alumno(models.Model):
    nombre = models.CharField(max_length=200)
    email = models.CharField(max_length=150, null=True, blank=True)
    fk_ponderacion = models.ForeignKey('Ponderacion', on_delete=models.CASCADE, related_name="ponderacion", null=True, blank=True)

    def __str__(self):
        return self.nombre


class Clase(models.Model):
    fecha = models.DateField()
    fk_alumno = models.ForeignKey('Alumno', on_delete=models.CASCADE, related_name="alumno", null=True, blank=True)

    def __str__(self):
        return self.fecha
    


class Archivo_Lista(models.Model):
    archivo = models.FileField(upload_to='csv')

    def __str__(self) -> str:
        return self.archivo.name

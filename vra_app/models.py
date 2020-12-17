from django.db import models

# Create your models here.


class Seguros(models.Model):
    seguro_id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100,null=False, unique=False)
    estado = models.CharField(max_length=8, null=False)
    color = models.CharField(max_length=7)
    prima_minima = models.FloatField()

    def __str__(self):
        return self.nombre


class Coberturas(models.Model):
    descripcion = models.TextField(null=False, unique=False)
    estado = models.CharField(null=False, max_length=8)

    def __str__(self):
        return self.descripcion


class CoberturaSeguros(models.Model):
    seguro_id = models.ForeignKey(Seguros, on_delete=models.CASCADE, null=False)
    cobertura_id = models.ForeignKey(Coberturas, on_delete=models.CASCADE, null=False)
    valor = models.CharField(max_length=255)


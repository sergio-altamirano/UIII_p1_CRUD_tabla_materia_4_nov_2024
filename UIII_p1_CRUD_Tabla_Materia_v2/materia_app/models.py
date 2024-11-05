from django.db import models

# Create your models here.

class Materia(models.Model):
    codido=models.CharField(primary_key=True,max_length=6)
    nombre=models.CharField(max_length=100)
    credito=models.PositiveSmallIntegerField()

    def __str__(self):
        return self.nombre
    
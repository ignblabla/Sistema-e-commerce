from django.db import models

# Create your models here.
class Marca(models.Model):
    nombre = models.CharField(max_length=50)

class Producto(models.Model):
    nombre = models.CharField(max_length=50)
    precio = models.IntegerField()
    description = models.TextField()
    nuevo = models.BooleanField()
    marca = models.ForeignKey(Marca, on_delete=models.PROTECT)
    fecha_fabricación = models.DateField()

    def __str__(self):
        return self.nombre
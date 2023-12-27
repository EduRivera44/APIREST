from django.db import models

class Trabajador(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    direccion = models.CharField(max_length=100)
    AreaDeTrabajo = models.CharField(max_length=100)
    salario = models.IntegerField(default=0)

class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    descripcion = models.TextField()

class Categoria(models.Model):
    nombre = models.CharField(max_length=50)
    def __str__(self):
        return self.nombre

class Pelicula(models.Model):
    titulo = models.CharField(max_length=100)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)

class Tienda(models.Model):
    nombre = models.CharField(max_length=100)
    ingresos_arriendo = models.IntegerField(default=0)

class Reparacion(models.Model):
    modelo = models.CharField(max_length=100)
    fecha_registro = models.DateField()
    fecha_entrega = models.DateField(null=True, blank=True)
    costo_reparacion = models.IntegerField(default=0)
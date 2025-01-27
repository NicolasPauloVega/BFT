from django.db import models
from django.utils.timezone import now

# Create your models here.

class Usuario(models.Model):
    id = models.IntegerField(primary_key=True)
    rol = models.IntegerField(null=True, blank=True, default=2) # campo no obligatorio
    img = models.ImageField(upload_to='imagenes/', null=True, blank=True)
    nombre = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    total_puntos = models.IntegerField(default=1000)
    password = models.CharField(max_length=45)
    habilitacion = models.BooleanField(null=True, blank=True, default=True)

    def sumar_puntos(self, puntos):
        self.total_puntos += puntos
        self.save()
        
    def restar_puntos(self, puntos):
        if self.total_puntos - puntos >= 0:
            self.total_puntos -= puntos
            self.save()
        else:
            raise ValueError('No se puede restar más puntos de los disponibles.')
    
    def __str__(self):
        return f"{self.nombre} - Puntos: {self.total_puntos}"


class Categoria(models.Model):
    nombre = models.CharField(max_length=255)

    def __str__(self):
        return self.nombre


class Subcategoria(models.Model):
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, related_name="subcategorias")
    nombre = models.CharField(max_length=255)
    puntos_positivos = models.IntegerField(default=0)
    puntos_negativos = models.IntegerField(default=0)

    def __str__(self):
        return self.nombre

class Puntos(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name="transacciones")
    subcategoria = models.ForeignKey(Subcategoria, on_delete=models.CASCADE, related_name="puntos_relacionados")
    fecha = models.DateTimeField(default=now)
    puntos = models.IntegerField(default=1000)
    evidencia = models.ImageField(upload_to="evidencias/")

    def __str__(self):
        return f"{self.usuario} - {self.puntos} puntos en {self.subcategoria}"
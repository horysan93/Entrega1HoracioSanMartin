from django.db import models

# Create your models here.

class Juego(models.Model):
    nombre = models.CharField(max_length=50)
    categoria = models.CharField(max_length=50)
    calificacion = models.IntegerField()
    resena = models.CharField(max_length=500)

    def __str__(self):
        return self.nombre+" "+str(self.categoria)


class Integrante(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    cargo = models.CharField(max_length=50)
    email = models.EmailField()

    def __str__(self):
         return self.nombre+" "+self.cargo


class Donador(models.Model):
    nombre = models.CharField(max_length=50)
    nickname = models.CharField(max_length=50)
    email = models.EmailField()

    def __str__(self):
        return self.nombre+"-"+self.nickname


class Sugerencia(models.Model):
    nombre = models.CharField(max_length=50)
    categoria = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre


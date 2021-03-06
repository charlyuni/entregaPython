from django.db import models

class Curso(models.Model):
    name = models.CharField(max_length=40)
    camada = models.IntegerField()
    email = models.EmailField()

class Estudiante(models.Model):
    name = models.CharField(max_length=40)
    lastname = models.CharField(max_length=40)
    


class Profesor(models.Model):
    name = models.CharField(max_length=40)
    lastname = models.CharField(max_length=40)
    email = models.EmailField()
    place = models.CharField(max_length=40)

class Entregable(models.Model):
    nombre = models.CharField(max_length=40)
    end_date = models.DateField()
    sent = models.BooleanField()

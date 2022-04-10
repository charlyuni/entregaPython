from django.db import models


class formulario(models.Model):
    name = models.CharField(max_length=20)
    lasname = models.CharField(max_length=20)
    email_client = models.EmailField(max_length=254, default="Some String")
    phone = models.IntegerField()
    messege = models.CharField(max_length=20)

class producto(models.Model):
    name = models.CharField(max_length=40)
    descripcion = models.CharField(max_length=40)
    precio = models.IntegerField()
    stock = models.IntegerField()
    categoria = models.CharField(max_length=40)
    imagen= models.CharField(max_length=40)

class Carrito(models.Model):
    total = models.CharField(max_length=40)
    fecha_compra = models.DateField()
    tipo_envio  = models.CharField(max_length=40)

from django.db import models


class formulario(models.Model):
    name = models.CharField(max_length=20)
    lasname = models.CharField(max_length=20)
    email_client = models.EmailField(max_length=254, default="Some String")
    phone = models.IntegerField()
    messege = models.CharField(max_length=20)
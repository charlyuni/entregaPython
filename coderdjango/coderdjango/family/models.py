from django.db import models


class myFamily(models.Model):
    name = models.CharField(max_length=40)
    type= models.CharField(max_length=40)
    year = models.IntegerField()
    married = models.BooleanField()
    children = models.IntegerField()
    birthdays = models.DateField()




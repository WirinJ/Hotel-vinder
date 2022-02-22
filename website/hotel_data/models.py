from django.db import models

# Create your models here.
class City(models.Model):
    name = models.CharField(max_length=125)

class Hotel(models.Model):
    name = models.CharField(max_length=125)
    city = models.ForeignKey(City, on_delete=models.CASCADE)
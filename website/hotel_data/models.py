from django.db import models

# Create your models here.
class City(models.Model):
    name = models.CharField(max_length=125)

    def __str__(self):
        return self.name 

class Hotel(models.Model):
    name = models.CharField(max_length=125)
    hotel_tag = models.CharField(max_length=25)
    city = models.ForeignKey(City, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
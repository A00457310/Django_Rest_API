from django.db import models


# Create your models here.

class Hotel(models.Model):
    id = models.IntegerField(primary_key=True)
    hotel_name = models.CharField(max_length=20)
    address = models.CharField(max_length=100)
    rating = models.CharField(max_length=20)
    capacity = models.CharField(max_length=20)

    def _str_(self):
        return  self.id+self.hotel_name+self.address+self.rating+self.capacity



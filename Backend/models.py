from django.db import models


# Create your models here.


class DetailsDB(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)
    description = models.CharField(max_length=500, null=True, blank=True)
    price = models.IntegerField(null=True, blank=True)
    advprice = models.IntegerField(null=True, blank=True)
    roomimage1 = models.ImageField(upload_to="Room_images", null=True, blank=True)
    roomimage2 = models.ImageField(upload_to="Room_images", null=True, blank=True)
    roomimage3 = models.ImageField(upload_to="Room_images", null=True, blank=True)

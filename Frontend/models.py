from django.db import models

# Create your models here.

# Creating Models for Contact Us
class ContactDB(models.Model):
    name = models.CharField(max_length=50, null=True, blank=True)
    email= models.EmailField(max_length=50,null=True, blank=True)
    number = models.IntegerField(null=True, blank=True)

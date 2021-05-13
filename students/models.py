from django.db import models
from taclass.models import Taclass

# Create your models here.
class Students(models.Model):
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    username = models.CharField(max_length=100, primary_key=True)
    phone = models.CharField(max_length=100)
    email = models.EmailField()
    password = models.CharField(max_length=100)
    confirmpassword = models.CharField(max_length=100)
    
    def __str__(self):
        return self.username


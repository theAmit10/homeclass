from django.db import models


# Create your models here.
class Teachers(models.Model):
    username = models.CharField(max_length=300 ,primary_key=True, unique=True)
    firstname = models.CharField(max_length=300)
    lastname = models.CharField(max_length=300)
    email = models.EmailField()
    phone = models.CharField(max_length=300)
    password = models.CharField(max_length=300)
    confirmPassword = models.CharField(max_length=300)
    

    def __str__(self):
        return self.userName
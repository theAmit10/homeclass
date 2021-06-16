from django.db import models
from datetime import datetime
from teachers.models import Teachers


# Create your models here.
class Taclass(models.Model):

    subject = models.CharField(max_length=100, primary_key=True,unique=True)
    classname = models.CharField(max_length=100, default=subject)
    classimage = models.ImageField(upload_to='photos/%Y/%m/%d/')
    teachername = models.CharField(max_length=100)
    section = models.CharField(max_length=100)
    


    def __str__(self):
        return self.subject



    



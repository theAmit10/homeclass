from django.db import models
from datetime import datetime

# Create your models here.

class Assignment(models.Model):
    assignmentid = models.CharField(max_length=100 ,primary_key=True, unique=True,default=0)
    assignmentfile = models.FileField()
    assignmenttitle = models.CharField(max_length=100, blank=True)
    assignmentgivendate = models.DateTimeField(default=datetime.now, blank=True)
    assignmentsubmissindate = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.assignmenttitle

from django.db import models

# Create your models here.
class appointment(models.Model):
    fullname=models.CharField(max_length=200)
    email=models.EmailField(max_length=200)
    hospitalName=models.CharField(max_length=200)
    requestingdate=models.DateTimeField()
    datetime=models.DateTimeField()

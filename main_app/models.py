from django.db import models

# Create your models here.
class Project(models.Model):
    id=models.IntegerField(primary_key=True)
    name=models.CharField(max_length=200)
    password=models.CharField(max_length=200)
    age=models.CharField(max_length=200)
    address=models.CharField(max_length=200)
    gender=models.CharField(max_length=200)
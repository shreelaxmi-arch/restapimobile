from django.db import models

# Create your models here.
class Mobile(models.Model):
    Name=models.CharField(max_length=100)
    Color=models.CharField(max_length=100)
    Model=models.CharField(max_length=100)
    Price=models.IntegerField()

    
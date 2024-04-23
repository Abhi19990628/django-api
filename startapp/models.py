from django.db import models

class Employess(models.Model):
    name=models.CharField(max_length=50)
    email=models.EmailField()
    age=models.CharField(max_length=3)
    phone=models.CharField(max_length=10)
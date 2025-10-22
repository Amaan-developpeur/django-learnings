from django.db import models

# Create your models here.
class UserRegistration(models.Model):
    name = models.CharField(max_length=20)
    username = models.CharField(max_length=15, primary_key=True)
    password = models.CharField(max_length=10)
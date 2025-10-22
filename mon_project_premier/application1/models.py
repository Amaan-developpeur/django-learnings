from django.db import models

# Create your models here.

class Employee(models.Model):
    name = models.CharField(max_length=50)
    empno = models.IntegerField()
    salary = models.FloatField()

class Country(models.Model):
    country = models.CharField(max_length=50)  # You need max_length for CharField

class Capital(models.Model):
    capital = models.CharField(max_length=50)  # Also need max_length here
    country = models.OneToOneField(
        Country, 
        primary_key=True,  # Makes country the primary key for Capital
        on_delete=models.CASCADE
    )



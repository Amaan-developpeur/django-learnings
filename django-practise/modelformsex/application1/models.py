from django.db import models

# Create your models here.
class EmployeeTable(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    designation = models.CharField(max_length=50)
    salary = models.FloatField()

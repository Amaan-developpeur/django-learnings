from django.db import models


# Create your models here.
class EmployeeTable(models.Model):
    name = models.CharField(max_length=50)
    empid = models.CharField(max_length=50)
    salary = models.CharField(max_length=50)

    

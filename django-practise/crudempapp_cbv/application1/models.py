from django.db import models

# Create your models here.
class EmployeeTable(models.Model):
    name = models.CharField(max_length=50)
    empid = models.IntegerField(primary_key=True)
    salary = models.FloatField()
    role = models.CharField(max_length=50)

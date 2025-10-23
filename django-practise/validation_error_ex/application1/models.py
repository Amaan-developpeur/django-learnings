from django.db import models

# Create your models here.
class StudentTable(models.Model):
    name = models.CharField(max_length=50)
    rollno = models.IntegerField(primary_key=True)
    email = models.EmailField()
    phone = models.CharField(max_length=10)

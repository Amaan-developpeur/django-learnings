from django.db import models

# Create your models here.
class StudentModel(models.Model):
    name = models.CharField(max_length=50)
    age = models.IntegerField
    email = models.EmailField(primary_key=True)
    marks = models.FloatField()

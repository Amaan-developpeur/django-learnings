from django.db import models

# Create your models here.
class Person(models.Model):
    name = models.CharField(max_length=50)
    age = models.IntegerField()

class Passport(models.Model):
    passport_number = models.CharField(max_length=50)
    person = models.OneToOneField(
        Person,
        on_delete=models.CASCADE
    )

from django.db import models

class Teacher(models.Model):
    name = models.CharField(max_length=50)
    subject = models.CharField(max_length=50)

class Student(models.Model):
    name = models.CharField(max_length=50)
    teacher = models.ForeignKey(
        Teacher,
        on_delete=models.CASCADE
    )

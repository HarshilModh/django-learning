from django.db import models


# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=20)
    age = models.IntegerField()
    email = models.EmailField()
    isActive = models.BooleanField(default=True)
    password = models.CharField(max_length=20)
    rollno = models.IntegerField()

    class Meta:
        db_table = "student"
    
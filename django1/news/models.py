from django.db import models
from django.db import models

# Create your models here.

class News(models.Model):
    #id will be genrate
    title = models.CharField(max_length=200)
    description = models.TextField()
    pub_date = models.DateTimeField('date published')
    reporterName = models.CharField(max_length=200,default='Anonymous')
    trp = models.IntegerField(null=True)

    class Meta:
        db_table = 'news'

class Author(models.Model):
    #id
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=200,unique=True)
    age = models.IntegerField(null=False)

    class Meta:
        db_table = 'authors'

class Book(Author):
    bookName = models.CharField(max_length=200)
    bookprice = models.FloatField(null=False)
    publishDate = models.DateTimeField('date published')

    class Meta:
        db_table = 'books'

class Course(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()

    class Meta:
        db_table = 'courses'


class Student(models.Model):
    cource = models.ForeignKey(Course,on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    age = models.IntegerField(null=False)

    class Meta:
        db_table = 'students'


class Abc(models.Model):
    name = models.CharField(max_length=200)
    age = models.IntegerField(null=False)



# Create your models here.

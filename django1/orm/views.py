from django.shortcuts import render
from .models import Student
from django.db.models import *
# Create your views here.
def getStudentData(request):
    StudentList=Student.objects.all().values()
    Student1=Student.objects.filter(name__startswith="H").values()
    Student3=Student.objects.filter(name__endswith="M").values()
    # students3 = Student.objects.filter(age__lte=20).values()
    # students4 = Student.objects.filter(age__gte=20).values()
    # students3 = Student.objects.filter(age__exact=20).values()
    student3 = Student.objects.filter(password__contains='@').values()
    students6 = Student.objects.filter(age__range=(10,20)).values()
    students7 = Student.objects.filter(age__range=(21,30)).count()
    print(students7)

    students8 = Student.objects.all().aggregate(Sum('age'))
    print(students8)
    students9 = Student.objects.all().aggregate(Avg('age'))
    print(students9)  
    students10 = Student.objects.all().aggregate(Max('age'))
    print(students10)
    
    print(StudentList)
    return render(request, 'orm/studentList.html',{'StudentList':StudentList,"student":students7})
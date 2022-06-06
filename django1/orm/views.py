from django.shortcuts import render
from .models import Student
# Create your views here.
def getStudentData(request):
    StudentList=Student.objects.all().values()
    print(StudentList)
    return render(request, 'orm/studentList.html',{'StudentList':StudentList})
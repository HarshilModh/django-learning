from django.contrib import admin
from django.urls import path,include
from orm import views

urlpatterns = [
    
    path('list/',views.getStudentData,name='list'),
]

from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    return HttpResponse("Hello World")

def index(request):
    return render(request, 'index.html')

def foodblog(request):
    return render(request, 'foodblog.html')

def petblog(request):
    return render(request, 'petblog.html')

def techblog(request):
    return render(request, 'techblog.html')
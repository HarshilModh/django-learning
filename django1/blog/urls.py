from django.urls import path
from . import views
urlpatterns = [
#path('', views.home, name='home'),
path('', views.index, name='index'),
path('index', views.index, name='index'),
path("foodblog", views.foodblog, name="foodblog"),
path("petblog", views.petblog, name="petblog"),
path("techblog", views.techblog, name="techblog"),

]
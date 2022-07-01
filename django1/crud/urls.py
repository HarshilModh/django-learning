from django import views
from django.contrib import admin
from django.urls import path,include
from . import views

app_name = 'crud'

urlpatterns = [
    
    path('addplayer/', views.PlayerCreateView.as_view(), name='addplayer'),
    path('playerlist/', views.PlayerListView.as_view(), name='player_list'),
    path("deletePlayer/<int:pk>", views.PlayerDeleteView.as_view(), name="delete_player"),
]
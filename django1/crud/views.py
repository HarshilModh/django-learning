

from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.shortcuts import render
from .models import *

# Create your views here.


class PlayerListView(ListView):
    model = Player
    template_name ="crud/player_list.html"
    context_object_name = "players"
    
    
class PlayerCreateView(CreateView):
    model = Player
    fields = '__all__'   
    template_name = "crud/player_create.html"
    success_url = reverse_lazy('crud:player_list')
class PlayerDeleteView(DeleteView):
    model = Player
    template_name = "crud/player_delete.html"
    success_url = reverse_lazy('crud:player_list')
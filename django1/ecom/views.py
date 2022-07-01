from django.shortcuts import render
from django.views.generic.edit import CreateView,DeleteView,UpdateView
from django.views.generic import ListView
from dataclasses import field

from .models import Product

# Create your views here.

class Createproduct(CreateView):
    model= Product
    fields=['name','description','price','qty']
    template_name="products/create.html"
    success_url="/ecom/list"
    
class ListProduct(ListView):
     model= Product
     product=model.objects.all()
     template_name ="products/list.html"
     context_object_name="products"
     def get_context_data(self,**kwargs):
         context=super().get_context_data(**kwargs)
         context['product']=self.product
         print(context)
class DeleteProduct(DeleteView):
     model= Product
     template_name="products/delete.html"
     success_url="/ecom/list" 
        
class UpdateProduct(UpdateView):
    model= Product
    fields=['price','qty']
    template_name="products/update.html"
    success_url="/ecom/list"
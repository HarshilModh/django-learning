from django.urls import URLPattern, path
from . import views

urlpatterns=[
    path("create",views.Createproduct.as_view(),name="product_create"),
    path("list",views.ListProduct.as_view(),name="product_list"),
    path("delete/<int:pk>",views.DeleteProduct.as_view(),name="product_Delete"),
    path("update/<int:pk>",views.UpdateProduct.as_view(),name="product_update")
    
    
    
]
from django.urls import path 
from . import views 
from .views import product_detail, product_list

urlpatterns = [
    path('', views.product_list, name='product_list'), 
    path('<int:id>/', product_detail, name='product_detail')
]
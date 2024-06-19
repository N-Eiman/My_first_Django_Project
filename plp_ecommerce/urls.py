from django.urls import path
from . import views

app_name= 'plp_ecommerce'

urlpatterns  =   [
    path('product_list/', views.product_list, name='product_list'),
]
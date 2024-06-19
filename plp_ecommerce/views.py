from django.shortcuts import render
from .models import Product
#from django.http import HttpResponse

# Create your views here.
def product_list(request):
    products = Product.objects.all(),   #when the product table is requested, the person adding the product must mimic the table and call all objects in the table
    context = {                         #giving context to how a product will be created, the name or attributes given to the products must be set/created the way the person who created it has , hence 'products': products
        'products': products,
    }
    return render(request, 'plp_ecommerce/product_list.html', context)

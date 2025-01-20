from django.shortcuts import render
from products.models import Product

# Create your views here.

def contact_us(request):
    """ A view to return the index page """
    products = Product.objects.all()
    context = {
        'products': products,
    }
    return render(request, 'contact_us/contact_us.html', context)

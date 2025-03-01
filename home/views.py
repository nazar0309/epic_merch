from django.shortcuts import render
from products.models import Product


def index(request):
    """ A view to return the index page with 12 latest products """
    products = Product.objects.all().order_by('-id')[:12]  # Get latest 12

    context = {
        'products': products,
    }
    return render(request, 'home/index.html', context)





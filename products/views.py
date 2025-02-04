from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from .models import Product, Category
from .forms import ProductForm

# Create your views here.

def all_products(request):
    """ A view to show all products, including sorting and search queries """
    
    products = Product.objects.all()
    query = None
    categories = None
    brands = None 
    sort = None
    direction = None
    
    if request.GET:
        
        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey == 'name':
                sortkey = 'lower_name'
                products = products.annotate(lower_name=Lower('name'))

            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
            products = products.order_by(sortkey)
            
        if 'brand' in request.GET:
            brands = request.GET['brand'].split(',')
            products = products.filter(brand__in=brands)
            
        if 'category' in request.GET:
            category_names = request.GET['category'].split(',')
            products = products.filter(category__name__in=category_names)
            categories = [
                category.friendly_name for category in Category.objects.filter(name__in=category_names)
            ]

            
        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "You didn't enter any search criteria!")
                return redirect(reverse('products'))
            
            queries = Q(name__icontains=query) | Q(description__icontains=query)
            products = products.filter(queries)
            
    current_sorting = f'{sort}_{direction}'

    context = {
        'products': products,
        'search_term': query,
        'current_categories': categories, 
        'brands': brands,  
        'current_sorting': current_sorting,
    }



    return render(request, 'products/products.html', context)


def product_details(request, product_id):
    """ A view to show individual product details """
    product = get_object_or_404(Product, pk=product_id)
    related_products = Product.objects.filter(
        category=product.category).order_by('name')[:4]
    context = {
        'product': product,  # Pass as singular
        'related_products': related_products,
    }

    return render(request, 'products/product_details.html', context)

def add_product(request):
    """ Add a product to the store """
    form = ProductForm()
    template = 'products/add_product.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


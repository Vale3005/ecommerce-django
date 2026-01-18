from django.shortcuts import render, get_object_or_404
from .models import Product 
from django.db.models import Q

def product_list(request): 
    products = Product.objects.all()
    
    # Ricerca per navbar 
    query = request.GET.get('q')
    if query:
        products = products.filter(
            Q(name__icontains=query) | 
            Q(description__icontains=query)
        )
    
    return render(request, 'products/product_list.html', {
        'products': products,
        'query': query
    })

def product_detail(request, id): 
    product = get_object_or_404(Product, id=id)
    return render(request, 'products/product_detail.html', {'product': product})
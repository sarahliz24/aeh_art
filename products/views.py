from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from .models import Product

def all_products(request):
    '''
    A view to show all products, including sorting and search queries
    '''

    products = Product.objects.all()
    query = None

    if request.GET:
        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "Please enter some search criteria")
                return redirect(reverse('products'))

            queries = Q(title__icontains=query) | Q(description__icontains=query)
            products = products.filter(queries)

    context = {
        'products': products,
        'search_term': query,
    }


    return render(request, 'products/products.html', context)


def product_detail(request, artwork_id):
    '''
    A view to show detail of single piece of art
    '''

    product = get_object_or_404(Product, pk=artwork_id)

    context = {
        'product': product,
    }


    return render(request, 'products/product_detail.html', context)


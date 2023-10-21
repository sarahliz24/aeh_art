from django.shortcuts import render, get_object_or_404
from .models import Product

def all_products(request):
    '''
    A view to show all products, including sorting and search queries
    '''

    products = Product.objects.all()

    context = {
        'products': products,
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


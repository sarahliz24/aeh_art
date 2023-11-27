from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.db.models.functions import Lower

from .models import Product, Category
from .forms import ProductForm
from profiles.models import UserProfile
from wishlist.models import Wishlist


def all_products(request):
    '''
    A view to show all products, including sorting and search queries
    '''
    products = Product.objects.all()
    query = None
    categories = None
    sort = None
    direction = None

    if request.GET:
        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey == 'title':
                sortkey = 'lower_title'
                products = products.annotate(lower_title=Lower('title'))
            if sortkey == 'category':
                sortkey = 'category__name'
            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
            products = products.order_by(sortkey)

        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            products = products.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)

        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "Please enter some search criteria")
                return redirect(reverse('products'))

            queries = (
                Q(title__icontains=query) | Q
                (description__icontains=query)
                )
            products = products.filter(queries)

    current_sorting = f'{sort}_{direction}'

    context = {
        'products': products,
        'search_term': query,
        'current_categories': categories,
        'current_sorting': current_sorting,
    }

    return render(request, 'products/products.html', context)


def product_detail(request, artwork_id):
    '''
    A view to show detail of single piece of art
    '''

    product = get_object_or_404(Product, pk=artwork_id)

    if not request.user.is_authenticated:
        template = "products/product_detail.html"
        context = {
            "product": product,
        }
        return render(request, template, context)

    else:
        user = get_object_or_404(UserProfile, user=request.user)
        wishlist = Wishlist.objects.filter(
            user=user, product=artwork_id)

        context = {
            'product': product,
            "wishlist": wishlist,
        }

    return render(request, 'products/product_detail.html', context)


@login_required
def add_product(request):
    """ Add artwork to the products page """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, this is for authorised users only')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save()
            messages.info(request, 'Artwork added successfully')
            return redirect(reverse(
                            'product_detail', args=[product.artwork_id]))
        else:
            messages.error(request, 'Failed to add artwork.\
                           Please check that the form is valid.')
    else:
        form = ProductForm()

    template = 'products/add_product.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


@login_required
def edit_product(request, artwork_id):
    """ Edit artwork from the products page """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, this is for authorised users only')
        return redirect(reverse('home'))

    product = get_object_or_404(Product, pk=artwork_id)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            messages.info(request, 'Artwork updated')
            return redirect(reverse(
                            'product_detail', args=[product.artwork_id]))
        else:
            messages.error(request, 'Artwork update failed. Please\
                           check that the form is valid.')
    else:
        form = ProductForm(instance=product)
        messages.info(request, f'You are editing {product.title}')

    template = 'products/edit_product.html'
    context = {
        'form': form,
        'product': product,
    }

    return render(request, template, context)


@login_required
def delete_product(request, artwork_id):
    """ Delete artwork from the products page """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, this is for authorised users only')
        return redirect(reverse('home'))

    product = get_object_or_404(Product, pk=artwork_id)
    product.delete()
    messages.success(request, 'Artwork deleted')
    return redirect(reverse('products'))

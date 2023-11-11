from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from profiles.models import UserProfile
from products.models import Product
from wishlist.models import Wishlist


@login_required
def wishlist(request):
    ''' Display wishlist to user '''

    user = get_object_or_404(UserProfile, user=request.user)
    wishlist = Wishlist.objects.filter(user=user)

    template = 'wishlist/wishlist.html'
    context = {"wishlist": wishlist}
   
    return render(request, template, context)


@login_required
def wishlist_add(request, artwork_id):
    ''' Add item to wishlist'''

    user = get_object_or_404(UserProfile, user=request.user)
    product = get_object_or_404(Product, pk=artwork_id)

    Wishlist.objects.create(user=user, pk=artwork_id)
    messages.success(request, f"{product.title} added to wishlist")
 
    return redirect(reverse("product_detail", args=[product.artwork_id]))


@login_required
def wishlist_remove(request, artwork_id):
    ''' Remove item from wishlist'''

    user = get_object_or_404(UserProfile, user=request.user)
    product = get_object_or_404(Product, pk=artwork_id)

    Wishlist.objects.filter(user=user, product=product).delete()
    messages.success(request, f"{product.title} removed from wishlist")
 
    return redirect(reverse("product_detail", args=[product.artwork_id]))

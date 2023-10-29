from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm


def checkout(request):
    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, "Your shopping bag is empty")
        return redirect(reverse('products'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51NtVHjEJxs6RYT2jp287dgzKIAf7zj3FYvpRKw3DfvkughYSkvNQXF3RMRDjYlXLmwu8Vw1QLIHkSHUDHwZt85fh00rJ44DiTl',
        'client_secret': 'test client secret',
    }

    return render(request, template, context)

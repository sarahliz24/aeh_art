from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models.functions import Lower

from .models import Newsletter
from .forms import NewsletterForm
from profiles.models import UserProfile


def newsletter(request):
    """ A view to return newsletter page """

    newsletter = Newsletter.objects.all()
   
    context = {
        'newsletter': newsletter,
    }

    return render(request, 'newsletter/newsletter.html', context)


def newsletter_detail(request, newsletter_id):
    '''
    A view to show detail of single newsletter
    '''

    newsletter = get_object_or_404(Newsletter, pk=newsletter_id)

    pass


@login_required
def add_newsletter(request):
    """ Add newsletter to the newsletter page """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, this is for authorised users only')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = NewsletterForm(request.POST, request.FILES)
        if form.is_valid():
            newsletter = form.save()
            messages.success(request, 'Newsletter added successfully')
            return redirect(reverse(
                            'newsletter', args=[newsletter.newsletter_id]))
        else:
            messages.error(request, 'Failed to add newsletter. Please check that the form is valid.')
    else:
        form = NewsletterForm()
       
    template = 'newsletter/add_newsletter.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


@login_required
def edit_newsletter(request, newsletter_id):
    """ Edit newsletter from the newsletter page """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, this is for authorised users only')
        return redirect(reverse('home'))

    product = get_object_or_404(Newsletter, pk=newsletter_id)
    if request.method == 'POST':
        form = NewsletterForm(request.POST, request.FILES, instance=newsletter)
        if form.is_valid():
            form.save()
            messages.success(request, 'Newsletter updated')
            return redirect(reverse(
                            'newsletter', args=[newsletter.newsletter_id]))
        else:
            messages.error(request, 'Newsletter update failed. Please check that the form is valid.')
    else:
        form = NewsletterForm(instance=newsletter)
        messages.info(request, f'You are editing {newsletter.title}')

    template = 'newsletter/edit_newsletter.html'
    context = {
        'form': form,
        'newsletter': newsletter,
    }

    return render(request, template, context)


@login_required
def delete_newsletter(request, newsletter_id):
    """ Delete newsletter from the newsletter page """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, this is for authorised users only')
        return redirect(reverse('home'))

    product = get_object_or_404(Newsletter, pk=newsletter_id)
    product.delete()
    messages.success(request, 'Newsletter deleted')
    return redirect(reverse('newsletter'))
from django.shortcuts import render, get_object_or_404
from .models import Awards
from django.core.paginator import Paginator, EmptyPage


def awards(request, page=1):
    """ A view to return awards page, with pagination"""
    awards = Awards.objects.all()
    paginator = Paginator(awards, 5)

    try:
        awards = paginator.page(page)
    except EmptyPage:
        # if we exceed the page limit we return the last page
        awards = paginator.page(paginator.num_pages)

    context = {
        'awards': awards,
    }

    return render(request, 'awards/awards.html', context)

from django.shortcuts import render, get_object_or_404
from .models import Publications
from django.core.paginator import Paginator, EmptyPage


def publications(request, page=1):
    """ A view to return publications page """
    publications = Publications.objects.all()
    paginator = Paginator(publications, 5)

    try:
        publications = paginator.page(page)
    except EmptyPage:
        # if we exceed the page limit we return the last page 
        publications = paginator.page(paginator.num_pages)

    context = {
        'publications': publications,
    }

    return render(request, 'publications/publications.html', context)

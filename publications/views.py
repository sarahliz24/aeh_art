from django.shortcuts import render, get_object_or_404
from .models import Publications
from django.core.paginator import Paginator


def publications(request):
    """ A view to return publications page """

    publications = Publications.objects.all()

    context = {
        'publications': publications,
    }

    return render(request, 'publications/publications.html', context)

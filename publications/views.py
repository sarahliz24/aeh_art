# from django.shortcuts import render


# def publications(request):
#     """ A view to return publications page """

#     return render(request, 'publications/publications.html')


from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.db.models.functions import Lower

from .models import Publications


def publications(request):
    """ A view to return publications page """

    publications = Publications.objects.all()
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
                return redirect(reverse('publications'))

            queries = Q(title__icontains=query) | Q(description__icontains=query)
            publications = publications.filter(queries)
    
    current_sorting = f'{sort}_{direction}'

    context = {
        'publications': publications,
        'search_term': query,
        'current_categories': categories,
        'current_sorting': current_sorting,
    }

    return render(request, 'publications/publications.html', context)

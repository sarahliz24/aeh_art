from django.shortcuts import render


def about(request):
    '''
    A view to return the about page
    '''
    return render(request, 'pages/about.html')


def artist(request):
    '''
    A view to return the artist page
    '''
    return render(request, 'pages/artist.html')


def scientist(request):
    '''
    A view to return the acientist page
    '''
    return render(request, 'pages/scientist.html')


def human(request):
    '''
    A view to return the human page
    '''
    return render(request, 'pages/human.html')


def shop_info(request):
    '''
    A view to return the shop info page
    '''
    return render(request, 'pages/shop_info.html')

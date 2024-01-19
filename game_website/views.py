from django.shortcuts import render


def homepage(request):
    return render(request, 'home.html')

def projects( request ):
    return render(request, 'portfolio.html')

def aboutme( request ):
    return render(request, 'home.html')

def blog( request ):
    return render(request, 'home.html')

def babblevoice( request ):
    return render(request, 'babblevoice.html')

def experimentio( request ):
    return render(request, 'experimentio.html')

def srmt( request ):
    return render(request, 'srmt.html')

def game( request ):
    return render(request, 'game.html')

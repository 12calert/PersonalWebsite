from django.views.generic import TemplateView
from accounts import models
from django.shortcuts import render
from django.http import JsonResponse
from django.http import HttpResponse
from django.db.models import F


from django.core import serializers


class PaypalReturnView(TemplateView):
    template_name = 'paypal_success.html'


class PaypalCancelView(TemplateView):
    template_name = 'paypal_cancel.html'

def homepage(request):
    users = models.CustomUser.objects.filter()
    user_names = []
    for user in users:
        user_names.append((user.nickname, user.description))
    context = { 'user_names': user_names }
    return render(request, 'home.html')

def projects( request ):
    return render(request, 'portfolio.html')

def aboutme( request ):
    return render(request, 'home.html')

def blog( request ):
    return render(request, 'home.html')

def babblevoice( request ):
    return render(request, 'babblevoice.html')

def game1( request ):
    return render(request, 'game1.html')

def get_users(request):
    users = models.CustomUser.objects.filter()
    print(serializers.serialize('json', users))
    return JsonResponse( serializers.serialize('json', users), safe=False )

def add_friend(request):
    user = models.CustomUser.objects.get(username=request.user)
    new_friends = user.friends
    new_friends[request.GET["id"]] = request.GET["id"]
    models.CustomUser.objects.filter(username=request.user).update(friends=new_friends)
    return HttpResponse("ok")
  
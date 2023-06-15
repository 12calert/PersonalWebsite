# accounts/views.py
import json
from uuid import uuid4
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
from django.shortcuts import render
from accounts import models
from django.views.generic import FormView
from django.urls import reverse
from django.shortcuts import redirect
from paypal.standard.forms import PayPalPaymentsForm
from accounts.forms import RegisterForm
from accounts.forms import AccountForm
from accounts.forms import ImageForm
from django.contrib.auth import authenticate
from django.contrib.auth import login
from django.contrib import messages
from accounts.models import CustomUser
from accounts.models import LeagueAccount
import accounts.riot as riot
import requests
import json
import random

def myaccount(request):
    new_post = models.Post(name="example post", user=request.user, content="I won a tournament", date="2022-12-12")
    #new_post.save()
    user = models.CustomUser.objects.get(username=request.user)
    posts = models.Post.objects.filter(user=request.user)
    profile_picture = models.GalleryImage.objects.filter()[0]
    context = { 'userinfo': user, 'posts': posts, "profile_picture": profile_picture }

    league_accounts = models.LeagueAccount.objects.filter(user=request.user)[0]

    data = riot.league_by_puuid(league_accounts.puuid, league_accounts.region)
    if ( "name" in data.keys() ):
        profile_icon = "images/riot/10.10.3224670/img/profileicon/" + "0.png"#str(data["profileIconId"]) + ".png"
        context = {'userinfo': user, 'posts': posts, "icon_path": profile_icon, "name": data["name"], "level": data["summonerLevel"]}

        data2 = riot.league_by_summoner( data["id"], league_accounts.region )
        for queue in data2:
            if queue["queueType"] == "RANKED_SOLO_5x5":
                context["tier"] = queue["tier"]
                context["rank"] = queue["rank"]
                context["lp"] = queue["leaguePoints"]
                break
    return render(request, 'myaccount.html', context=context)


class PaypalFormView(FormView):
    template_name = 'paypal_form.html'
    form_class = PayPalPaymentsForm

    def get_initial(self):
        return {
            "business": 'your-paypal-business-address@example.com',
            "amount": 20,
            "currency_code": "GBP",
            "item_name": 'Example item',
            "invoice": 1234,
            "notify_url": self.request.build_absolute_uri(reverse('paypal-ipn')),
            "return_url": self.request.build_absolute_uri(reverse('paypal-return')),
            "cancel_return": self.request.build_absolute_uri(reverse('paypal-cancel')),
            "lc": 'EN',
            "no_shipping": '1',
        }

def register(request):
	if request.method == "POST":
		form = RegisterForm(request.POST)
		if form.is_valid():
			user = form.save()
			user.set_password(request.POST['password'])
			user.save()
			new_user = CustomUser(username=user, nickname=form.cleaned_data['nickname'], email=form.cleaned_data['email'], user_id=uuid4(), friends={}, description="")
			new_user.save()
			login(request, user)
			messages.success(request, "Registration successful." )
			return redirect("/home")
		messages.error(request, "Unsuccessful registration. Invalid information.")
	form = RegisterForm()
	return render (request=request, template_name="registration/signup.html", context={"register_form":form})

def settings(request):
    if request.method == "POST":
        if "image_upload" in request.POST.keys():
            form = ImageForm(request.POST, request.FILES)
            if form.is_valid():
                form = form.save(commit=False)
                form.user = request.user
                form.save()
        else:
            form = AccountForm(request.POST)
            if form.is_valid():
                data = riot.league_by_name( form.cleaned_data['name'], riot.translate_selection_region(form.cleaned_data['region']) )
                if ( "profileIconId" in data.keys() ):
                    if ( data["profileIconId"] == request.session["icon_number"] or True ):
                        if ( len(models.LeagueAccount.objects.filter(puuid=data["puuid"])) == 0 ):
                            new_account = LeagueAccount( user=request.user, puuid=data["puuid"], hashed_id=data["accountId"], region=form.cleaned_data['region'] )
                            new_account.save()
                            messages.success(request, "Registration successful." )
                            return redirect("/accounts/myaccount")
                        else:
                            messages.error(request, "Account already registered")
                    else:
                        messages.error(request, "Incorrect profile icon")
                else:
                    messages.error(request, "Summoner not found")
            else:
                messages.error(request, "Invalid information.")
    account_form = AccountForm()
    image_form = ImageForm()
    icon_number = random.randint(0,28)
    icon_path = "images/riot/10.10.3224670/img/profileicon/" + f"{icon_number}" + ".png"
    request.session["icon_number"] = icon_number
    return render (request=request, template_name="settings/settings.html", context={"account_form":account_form, "image_form":image_form, "icon_path": icon_path})

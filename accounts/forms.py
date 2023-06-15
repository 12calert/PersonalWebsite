from django.contrib.auth.models import User
from django import forms
from accounts import models


class RegisterForm(forms.ModelForm):
    username = forms.CharField(max_length=100, label="Login")
    password = forms.CharField(widget=forms.PasswordInput())
    email = forms.CharField(widget=forms.EmailInput())
    nickname = forms.CharField(max_length=100, label='Nick')

    class Meta:
        model = User
        fields = ["username", "password", "email", "nickname"]

class AccountForm(forms.ModelForm):
    REGION_CHOICES = (
    ("1", "EUNE"),
    ("2", "EUW"),
    ("3", "NA"),
    ("4", "KR"),
    ("5", "BR"),
    ("6", "JP"),
    ("7", "OC"),
    ("8", "LA1"),
    ("9", "LA2"),
    ("10", "RU"),
    ("11", "TR"),
    )
    name = forms.CharField(max_length=100, label="League of Legends account name")
    region = forms.ChoiceField(choices=REGION_CHOICES)

    class Meta:
        model = models.LeagueAccount
        fields = ["name", "region"]

class ImageForm(forms.ModelForm):

    class Meta:
        model = models.GalleryImage
        fields = ["user", "image"]

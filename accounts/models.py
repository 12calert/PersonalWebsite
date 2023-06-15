from django.db import models
from django.conf import settings
from jsonfield import JSONField

# Create your models here.

class CustomUser(models.Model):

    username = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default="")
    user_id = models.TextField()
    friends = JSONField()
    nickname = models.TextField()
    description = models.TextField()
    profile_picture = models.ImageField(default="", upload_to='images/')
    email = models.EmailField(default="")
    sex = models.TextField(default="male")
    age = models.IntegerField(default=20)

class Post(models.Model):
    name = models.TextField()
    content = models.TextField()
    date = models.DateField()
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default="")
    post_image = models.ImageField(default="")

class LeagueAccount(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    puuid = models.TextField()
    hashed_id = models.TextField()
    region = models.TextField( default="EUNE" )

class GalleryImage(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    image = models.ImageField(default="")
    
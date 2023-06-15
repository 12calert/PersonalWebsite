"""game_website URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import TemplateView
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.staticfiles.storage import staticfiles_storage
from django.views.generic.base import RedirectView
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls'), name='accounts'),
    path('accounts/', include('django.contrib.auth.urls'), name='accounts'),
    path('', TemplateView.as_view(template_name='home.html'), name='home'),
    path('home', views.homepage, name='home'),
    path('get_users', views.get_users, name='get_users'),
    path('add_friend', views.add_friend, name='add_friend'),
    path('download', TemplateView.as_view(template_name='download.html'), name='download'),
    path('paypal/', include('paypal.standard.ipn.urls')),
    path('paypal-return/', views.PaypalReturnView.as_view(), name='paypal-return'),
    path('paypal-cancel/', views.PaypalCancelView.as_view(), name='paypal-cancel'),
    path('favicon.ico', RedirectView.as_view(url=staticfiles_storage.url('images/favicon.ico')))

]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)
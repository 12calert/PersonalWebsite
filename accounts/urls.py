# accounts/urls.py
from django.urls import path, include

from . import views

app_name= 'accounts'

urlpatterns = [
    path('signup/', views.register, name='signup'),
    path('myaccount/', views.myaccount, name='myaccount'),
    path('paypal/', include('paypal.standard.ipn.urls')),
    path('buy_game', views.PaypalFormView.as_view(), name='buy_game'),
    path('settings', views.settings, name='settings'),
]
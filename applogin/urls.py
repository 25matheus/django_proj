from django import views
from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    #mapping the urls
    path('', views.home, name="home"),
    path('signup', views.signup, name="signup"),
    path('signin', views.signin, name="signin"),
    path('signout', views.signout, name="signout"),
]

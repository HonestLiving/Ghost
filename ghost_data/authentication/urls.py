from django.contrib import admin
from django.urls import path, include 
from . import views

urlpatterns = [
    path('',views.login, name="login"),
    path('signup.html', views.signup, name="signup"),
    path('signout', views.signout, name="signout"),
]

from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def login(request):
    return render(request, "authentication/index.html")

def signup(request):
    return render(request, "authentication/signup.html")

def home(request):
    return render (request, "authentication/home.html")

def signout(request):
    pass
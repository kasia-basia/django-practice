from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def index(request):
    return render(request, 'pages/index.html')


def about(request):
    return render(request, 'pages/about.html')


def login(request):
    return render(request, 'pages/login.html')


def listings(request):
    return render(request, 'pages/listings.html')

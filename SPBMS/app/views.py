from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *


def home(request):
    return render(request,'home.html')

def login(request):
    return render(request,'login.html')

def register(request):
    if request.method == "POST":
        first_name = request.POST.get('first-name')
        last_name = request.POST.get('last-name')
        username =  request.POST.get('username')
    return render(request,'Registration.html')
from django.shortcuts import render, redirect
from django.http import HttpResponse,JsonResponse
from django.contrib.auth import authenticate, login ,logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import *
from django.urls import reverse


def home(request):
    return render(request,'home.html')

def logIn(request):
    # data = request.POST
    # print(data)
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        # print(f'user:{username} pass: {password}')

        if not User.objects.filter(username=username).exists():
            messages.error(request,'Invalid username')
            return redirect('signin')
        
        user = authenticate(username=username,password=password)

        if user is None:
            messages.error(request, 'Invalid password')
            return redirect('signin')
        
        else:
            login(request,user)
            return redirect(reverse('dashboard'))

    return render(request,'login.html')

def checkUsername(request):
    username = request.GET.get('username', '')
    is_unique = not User.objects.filter(username=username).exists()
    return JsonResponse({'is_unique':is_unique})

def logOut(request):
    logout(request)
    return redirect('home')

def register(request):
    if request.method == "POST":
        first_name = request.POST.get('first-name')
        last_name = request.POST.get('last-name')
        username =  request.POST.get('username')
        password = request.POST.get('password')
        profile_picture = request.FILES.get('profile-picture')

        if User.objects.filter(username=username).exists():
            messages.error(request,'User already exists')
            return redirect('register')

        user = User.objects.create_user(
            username=username,
            password=password,
            first_name=first_name,
            last_name=last_name
        )
        if profile_picture:
            user.profile_picture = profile_picture

        user.save()

        messages.success(request,"User Registered")
        return redirect('signin')

    return render(request,'Registration.html')

@login_required(login_url='/login/')
def dashboard(request):
    return render(request,'dashboard.html') 

def budget(request):
    if request.method == "POST":
        monthly_income = request.POST.get('monthly-income')
        total_expenses = request.POST.get('total-expenses')
        category_name = request.POST.get('category-name')
        


    return render(request, 'expense.html')
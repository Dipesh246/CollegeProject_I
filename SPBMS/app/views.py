from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.contrib.auth import authenticate, login ,logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import *
from django.urls import reverse
import decimal,json
from django.db.models import Sum
from django.contrib.auth.forms import PasswordResetForm


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
        # print(user)

        if user is None:
            messages.error(request, 'Invalid username or password')
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
        email = request.POST.get('email')
        phone_number = request.POST.get('phone')
        profile_picture = request.FILES.get('profile-picture')

        if User.objects.filter(username=username).exists():
            messages.error(request,'User already exists')
            return redirect('register')

        user = User.objects.create(
            username=username,
            password=password,
            first_name=first_name,
            last_name=last_name,
            email= email,
            phone_number=phone_number
        )
        user.set_password(password)
        if profile_picture:
            user.profile_picture = profile_picture

        user.save()

        messages.success(request,"User Registered")
        return redirect('signin')

    return render(request,'Registration.html')



@login_required(login_url='/login/')
def dashboard(request):
    total_savings = 0
    data = []
    budgets = Budeget.objects.all()
    
    for budget in budgets:
        categories = Category.objects.filter(budget=budget)

        for category in categories:
            total_spendings = Expense.objects.filter(budget=budget,category=category,date__lte=budget.end_date).aggregate(Sum('amount'))['amount__sum'] or 0
            allocated_amount = category.allocated_amount
            if allocated_amount==None:
                savings = total_spendings
            else:    
                savings = allocated_amount - total_spendings
            total_savings +=savings
            data.append({
                'category':category.category_name,
                'total_spendings':float(total_spendings),
                'total_savings':float(total_savings)
            })
    budgets_json = json.dumps([{'name': budget.budget_name, 'total_budget': float(budget.monthly_income)} for budget in budgets])
    # print(budgets_json)
    # print(json.dumps(data))       

    context = {
        'budgets_data_json': budgets_json,
        'data_json': json.dumps(data),
    }
    

    return render(request,'dashboard.html',context) 

def budget(request):
    user_budgets = Budeget.objects.filter(user = request.user)
    categories = Category.objects.all()
    
    return render(request, 'expense.html',{'user_budgets':user_budgets,
                                           'categories':categories})
    

def saveBudget(request):
    current_user = request.user
    if request.method == "POST":
        budget_name =  request.POST.get('budget-name')
        monthly_income = request.POST.get('monthly-income')
        start_date = request.POST.get('start_date')
        end_date = request.POST.get('end_date')

        if decimal.Decimal(monthly_income)<1000:
            messages.error(request,"Budget amount must be more then Rs. 1000")
            return redirect('budget')
        else:
            budget = Budeget.objects.filter(budget_name=budget_name)
            if budget:
                Budeget.objects.filter(budget_name=budget_name).update(monthly_income=monthly_income,
                                                                                    start_date=start_date,
                                                                                    end_date=end_date)
                return redirect('budget')
            else:    
                budget = Budeget.objects.create(user=current_user,
                                                budget_name=budget_name,
                                                monthly_income=monthly_income,
                                                start_date=start_date,
                                                end_date=end_date)
                budget.save()
                return redirect('budget')
    
def saveCategory(request):
    if request.method == "POST":
        category_name = request.POST.get('category_name')
        allocated_amount = request.POST.get('budget_amount')
        budget_id = request.POST.get('budget')

        user_budget = Budeget.objects.filter(user = request.user , id = budget_id).first()
        
        
        if category_name:
            category= Category.objects.create(category_name=category_name, budget = user_budget)
            # print('qry: ', category.query)
            category.save()
        
        if allocated_amount:
            category_name = request.POST.get('category')
            category = Category.objects.filter(category_name=category_name).update(allocated_amount=allocated_amount)
        else:
            category = Category.objects.filter(category_name=category_name).update(allocated_amount=0)
        
        

        return redirect('budget')
    
def spendings(request):
    categories = Category.objects.all()

    if request.method == "POST":
        for category in categories:
            date = request.POST.get(f'{category.category_name}_date')
            amount = request.POST.get(f'{category.category_name}_amount')

            if date and amount:
                last_expense = Expense.objects.filter(category=category).last()
                
                if last_expense:
                    reamining_amount  = last_expense.remaining_amount - decimal.Decimal(amount)
                elif category.allocated_amount==None:
                    reamining_amount = decimal.Decimal(amount)
                else:
                    reamining_amount = category.allocated_amount - decimal.Decimal(amount)    

                expense = Expense.objects.create(budget = category.budget,
                                                 category = category,
                                                 remaining_amount=reamining_amount,
                                                 amount = amount,
                                                 date = date)
                expense.save()

        return redirect('spendings') 
    else:       
        context = {"categories":categories}    
        return render(request,'spendings.html',context)    
    
    
def budget_reports(request):
    spendings = Expense.objects.all()
    savings_data = []
    budgets = Budeget.objects.all()
    for budget in budgets:
        categories = Category.objects.filter(budget=budget)

        
        for category in categories:
            print(category)
            total_spendings = Expense.objects.filter(budget=budget,category=category,date__lte=budget.end_date).aggregate(Sum('amount'))['amount__sum']or 0
            allocated_amount = category.allocated_amount
            if allocated_amount==None:
                savings = total_spendings
            else:    
                savings = allocated_amount - total_spendings
            savings_data.append({
                'category':category.category_name,
                'allocated_amount':allocated_amount,
                'total_spending':total_spendings,
                'savings':savings,
            })

            
    
    context = {'spendings':spendings,
               'savings_data':savings_data}
    # print(context)
    return render(request,'reports.html',context) 

def forgetPassword(request):
    form = PasswordResetForm(request.POST or None)
    if request.method =="POST":
        
        if form.is_valid():
            form.save(request=request)
            messages.success(request,'Password Reset email sent. Please check your email.')
            return redirect('signin')
        else:
            print("entered")
            form = PasswordResetForm()

    return render(request, 'forgetpassword.html', {'form':form})


    
    
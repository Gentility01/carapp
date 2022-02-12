from urllib import request
from django.shortcuts import render, redirect
from django.http import HttpResponse

# from Accounts.models import MainStaff
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from .forms import CustomerSignupForm, MainStaffCreationForm
from django.contrib.auth import login, logout, authenticate
from .models import Customer


# Create your views here.

def show_customers(request):
    customer = Customer.objects.all()
    context = {
        'customer':customer
    }
    return render(request, 'Accounts/show_customers.html', context)

def dashboard(request):
    return render(request, 'Accounts/dashboard.html')


def login_view(request):
    return render(request, 'Accounts/login.html')

def customer_register(request):
    form = CustomerSignupForm()
    if request.method == 'POST':
        form = CustomerSignupForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            email = form.cleaned_data.get("email")
            password = form.cleaned_data.get("password1")
            form.save()
            new_user = authenticate(username=username, email=email, password=password)
            if new_user is not None:
                login(request, new_user)
                return redirect("product:product_list")

    else:
        form = CustomerSignupForm()
        
    context = {
            'form':form
        }
    return render(request, 'Accounts/customer_register.html', context )

    
def customer_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('product:product_list')
            else:
                messages.error(request, 'Inalid Username or password')
        else:
            messages.error(request, 'Inalid Username or password')
    context={
        'form':AuthenticationForm()
    }
    return render(request, 'Accounts/customer_login.html', context)



def mainstaff_register(request):
    form = MainStaffCreationForm()
    if request.method == 'POST':
        form = MainStaffCreationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            email = form.cleaned_data.get("email")
            password = form.cleaned_data.get("password1")
            form.save()
            new_user = authenticate(username=username, email=email, password=password)
            if new_user is not None:
                login(request, new_user)
                return redirect('dashboard')
            
    else:
        form = MainStaffCreationForm()
    context = {
            'form':form
        }
    return render(request,'Accounts/admin_register.html', context)



def mainstaff_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('dashboard')
            else:
                messages.error(request, 'Inalid Username or password')
        else:
            messages.error(request, 'Inalid Username or password')
    context={
        'form':AuthenticationForm()
    }
    return render(request, 'Accounts/mainstaff_login.html', context)


def logout_view(request):
    logout(request)
    return redirect('login')
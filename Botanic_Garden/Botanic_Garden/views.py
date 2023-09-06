from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required


def homePage(request):
    
    return render(request, "homePage.html")

@login_required(login_url='login')
def plants(request):

    return render(request, "plants.html")

def register(request):
    if request.method == "POST":
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        rePassword = request.POST.get('rePassword')

        if password != rePassword:
            return HttpResponse("Password does not match!!!")
    
        myUser = User.objects.create_user(username, email, password)
        myUser.save()
        
        return redirect('/login')
        
        print(username, email, password, rePassword)
        
    return render(request, "register.html")

def loginPage(request):
    
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request,user)
            return redirect('/')
        
        else:
            return HttpResponse("Username or Password is incorrect")
            
        print(usernameL, passwordL)
    return render(request, "login.html")

def logoutPage(request):
    logout(request)
    return redirect('login')
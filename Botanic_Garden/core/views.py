from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
from .forms import *
from django.contrib import messages
from .models import *


def homePage(request):
    
    return render(request, "homePage.html")


def plants(request):

    return render(request, "plants.html")



def register(request):
    form=CreateUserForm()
        
    if request.method == "POST":
        print("Register")
        form = CreateUserForm(request.POST)
        
        if form.is_valid():
            
            form.save()
            firstName = form.cleaned_data.get('first_name')
            lastName = form.cleaned_data.get('last_name')
            username = form.cleaned_data.get('username')
            
            messages.success(request,"Account Created for " + username)
            
            return redirect('login')
    context={'form': form}
    
    
    return render(request, "register.html", context)

#  user = super(CreateUserForm, self).save(commit=False)

#         # Save the image if provided
#         if self.cleaned_data['profile_picture']:
#             user.profile.profile_picture = self.cleaned_data['profile_picture']
        
#         if commit:
#             user.save()
#         return user

def loginUser(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
            
            
        if user is not None:
            login(request, user)
             
            return redirect('/')

        else:
            messages.info(request, 'Username or Password is incorrect')

    return render(request, 'login.html')


def logoutPage(request):
    logout(request)
    return redirect('login')

@login_required(login_url='login')
def dashboard(request):
    form = UserUploadPlants
    
    if request.user.is_authenticated:
        first_name = request.user.first_name
        last_name = request.user.last_name
        
    AllItems = UserUploadPlants.objects.filter(user = request.user).order_by('-id')
    
    total_plants = UserUploadPlants.objects.filter(user=request.user).count()     
        
    context={
        'form': form,
        'AllItems': AllItems,
        'first_name': first_name,
        'last_name': last_name,
        }
     
    return render(request, "dashboard.html",context)

@login_required(login_url='login')
def addPlants(request):
    form = UserUploadedPlantForm()
    
    if request.method == 'POST':
        form = UserUploadedPlantForm(request.POST, request.FILES)
        
        if form.is_valid():
            instance = form.save(commit=False)  #commit false helps in not saving form
            instance.user = request.user
            instance.save()
            
            # Creating a new empty form instance
            messages.sucess(request, "Succesfully added new plant")
            
            return redirect('addPlants')
        
        else:
            return render(request, 'dashboard.html')
    
    context = {
        'form': form,
    }

    return render(request, 'dashboard.html', context)




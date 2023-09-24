from django.shortcuts import get_object_or_404, render

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
from django.urls import reverse
from .forms import *
from django.contrib import messages
from .models import *
from django.core.paginator import Paginator
from math import ceil

def homePage(request):
    
    return render(request, "homePage.html")



def plants(request, category=None):
    # Query the database to get the plants data
    plants_data = UserUploadPlants.objects.all()  # You can add filters if needed
    uploaded_user= request.POST.get("user")

    print("Number of plants retrieved:", len(plants_data))

    context = {
        'plants_data': plants_data,
    }
    
    if not plants_data:
        context['no_plants_message'] = "Sorry, There are currently no plants available"
    if request.method == 'POST':
        if "add" in request.POST:
            if not Cart.objects.filter(user=user_instance, item_id=plant_id).exists(): 
                    addToCart = Cart(plant_id=plant_id,title=plant_title,category=plant_category,price=plant_price,image=plant_image,user=user_instance)
                    addToCart.save()
    return render(request, "plants.html", context)



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
    form = UserUploadedPlantForm()
    #filter used to get the data of the user logged in only
    
    plants_data = UserUploadPlants.objects.filter(user = request.user)
    plants_data_first = UserUploadPlants.objects.filter(user=request.user).order_by('-id').first()
    if request.user.is_authenticated:
        first_name = request.user.first_name
    
    #filtering only items that is uploaded by current logged in user
    
    context={
        'form':form,
        'plants_data': plants_data,
        'first_name':first_name,
        'plants_data_first': plants_data_first
    } 
    
    if request.method == 'POST':
        form = UserUploadedPlantForm(request.POST, request.FILES)
        print("vayp")

        
        if form.is_valid():
            
            instance = form.save(commit=False) #commit=False helps to not to save the form
            instance.user = request.user
            instance.save()
        
            messages.success(request, "Successfully Added")
        
            return redirect('dashboard')
        else:
            print(form.errors)
    
    
    else:
        return render(request, 'dashboard.html', context)
    
    if not plants_data:
        print('vayena')
        context['no_plants_message'] = "Sorry, There are currently no plants available"
    
    return render(request, "dashboard.html", context)
    


@login_required(login_url='login')
def editPlant(request, plant_id):
    plant = get_object_or_404(UserUploadPlants, id=plant_id, user=request.user)
    form = UserUploadedPlantForm()
    #filter used to get the data of the user logged in only
    
    plants_data = UserUploadPlants.objects.filter(user = request.user)
    plants_data_first = UserUploadPlants.objects.filter(user=request.user).order_by('-id').first()
    if request.user.is_authenticated:
        first_name = request.user.first_name
    
    #filtering only items that is uploaded by current logged in user
    
    print(plant_id)
    if request.method == 'POST':
        form = UserUploadedPlantForm(request.POST, request.FILES, instance=plant)
        if form.is_valid():
            form.save()
            messages.success(request, "Plant updated successfully")
            return redirect('dashboard')
    else:
        form = UserUploadedPlantForm(instance=plant)

    context = {
        'form': form,
        'plant': plant,
        'plants_data': plants_data,
        'first_name':first_name,
        'plants_data_first': plants_data_first
    }
    return render(request, 'dashboard.html', context)

    
    #deleting item
@login_required(login_url="login")
def deletePlant(request, plant_id):
    
    plant = get_object_or_404(UserUploadPlants, id=plant_id, user=request.user)
    plant.delete()
    return redirect('dashboard')

def cart(request):
    
    cartPlant = Cart.objects.filter(user=request.user)
    
    # Calculating total price
    totalPrice=0
    for item in cartPlant:
        totalPrice += item.price
    
    totalPlant = cartPlant.count()

    if request.method == "POST":
        
        plant_id = request.POST.get("plant_id")
        DeletePlantCart = Cart.objects.get(id=plant_id, user=request.user)
        DeletePlantCart.delete()
        return redirect('cart')

    
    context={
        'cartPlant':cartPlant,
        'totalPlant':totalPlant,
        'totalPrice':totalPrice,

    }

    
    return render(request, 'cart.html', context)
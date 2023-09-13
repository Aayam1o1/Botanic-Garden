from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import User
from django import forms
from .models import *

class CreateUserForm(UserCreationForm):
    # user = forms.OneToOneField(User, on_delete=forms.CASCADE, related_name='CreateUserForm')
    # profile_picture = models.ImageField(upload_to = 'images', default = 'default.svg' )
    
    class Meta:
        model= User
        fields = ['first_name', 'last_name','username', 'email', 'password1', 'password2']


class UserUploadedPlantForm(ModelForm):
    class Meta:  # Capitalize "Meta"
        model = UserUploadPlants
        widgets = {
            'description': forms.Textarea(attrs={'rows':4, 'cols':15}),
            'price': forms.NumberInput(attrs={'min': 0, 'step': 0.01}),
        }
        exclude = ('user',)
        fields = "__all__"
        
        


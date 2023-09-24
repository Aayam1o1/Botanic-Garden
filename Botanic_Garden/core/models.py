from django.db import models
# Create your models here.
from django.db import models
from django.contrib.auth.models import User
# from .models import UserUploadedPlantForm  # Add this import at the top of your views file.


 #Category choices
categoryChoice = (
    ('Indoor', 'Indoor'),
    ('Outdoor', 'Outdoor'),
    ('Tropical', 'Tropical'),
    ('Pet Frienly', 'Pet Friendly'),
    ('Easy Care', 'Easy Care')
)
    
    
# creating plants uplaod

class UserUploadPlants(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    category = models.CharField(max_length=20,choices=categoryChoice, default='Indoor')
    image = models.ImageField(upload_to = "images/")    
    price = models.DecimalField(max_digits=10, decimal_places=2)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.title


class Cart(models.Model):
    title = models.CharField(max_length=100)
    category = models.CharField(max_length=100, choices=categoryChoice)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image= models.ImageField(upload_to = "cart/")
    plant_id=models.IntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.title
